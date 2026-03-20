import os
import httpx
from app.models.knowledge_base import DocStatus
from app.services.text_splitter import split_markdown_file

# Константы для интеграции
MCP_SERVER_NAME = "epicaltrendweb/notebooklm-mcp-v2"
SKILL_NAME = "PleasePrompto/notebooklm-skill"
NOTEBOOKLM_API_URL = os.getenv("NOTEBOOKLM_API_URL", "http://localhost:3030")


async def process_document_for_rag(doc_id: str, file_path: str, tool_name: str) -> str:
    """
    Интеграция с NotebookLM MCP сервером через HTTP REST API

    Вызывается когда документ переходит в статус "Загружается в RAG".
    1. Создает новый пустой блокнот с именем инструмента (tool_name).
    2. Добавляет блокнот во внутреннюю библиотеку MCP-сервера.
    3. При необходимости разбивает markdown-файл (file_path) на части, если он превышает лимиты (200 МБ / 500k слов).
    4. Загружает полученные файлы как источники в этот блокнот.
    5. Возвращает полученный от NotebookLM ID блокнота.
    """
    print(f"[RAG Service] Начинаем загрузку документации {tool_name} в NotebookLM...")

    # 1. Сначала разбиваем файл локально (в среде FastAPI)
    try:
        # 1. Мы больше НЕ разбиваем файл локально.
        # NotebookLM умеет съедать до 500k слов на источник.
        # file_path может прийти абсолютным с Windows или Docker. Проверяем существование
        local_file_path = file_path
        # Если запущено на Windows, но путь линуксовый (для тестов вне докера)
        if not os.path.exists(local_file_path) and "/app/docs" in local_file_path:
            local_file_path = local_file_path.replace("/app/docs", "../../docs_parsing")

        print(f"[RAG Service] Подготовка файла к загрузке: {local_file_path}")
        split_files = [local_file_path]  # Грузим целиком
    except Exception as e:
        print(f"[RAG Service] Ошибка при разбивке файла: {e}")
        raise

    async with httpx.AsyncClient(timeout=300.0) as client:  # Длинный таймаут
        try:
            notebook_id = None
            notebook_url = None

            # Проверяем, существует ли уже блокнот с таким именем в библиотеке
            print(f"[RAG Service] Проверяем наличие блокнота '{tool_name}'...")
            check_resp = await client.get(f"{NOTEBOOKLM_API_URL}/notebooks")
            if check_resp.status_code == 200:
                check_data = check_resp.json()
                if check_data.get("success"):
                    for nb in check_data.get("data", {}).get("notebooks", []):
                        if nb.get("name") == tool_name:
                            notebook_id = nb.get("id")
                            notebook_url = nb.get("url")
                            print(
                                f"[RAG Service] Блокнот '{tool_name}' уже существует. ID: {notebook_id}"
                            )
                            break

            if not notebook_id:
                # 2. Создание блокнота в Google NotebookLM
                print(f"[RAG Service] Создаем блокнот '{tool_name}'...")
                create_resp = await client.post(
                    f"{NOTEBOOKLM_API_URL}/notebooks/create", json={"name": tool_name}
                )
                create_resp.raise_for_status()
                create_data = create_resp.json()

                if not create_data.get("success"):
                    raise Exception(
                        f"Ошибка создания блокнота: {create_data.get('error')}"
                    )

                notebook_id = create_data["data"]["notebook_id"]
                notebook_url = create_data["data"]["notebook_url"]
                print(f"[RAG Service] Блокнот создан! ID: {notebook_id}")

                # 3. Добавление блокнота в локальную библиотеку MCP
                await client.post(
                    f"{NOTEBOOKLM_API_URL}/notebooks",
                    json={
                        "url": notebook_url,
                        "name": tool_name,
                        "description": f"Техническая документация для {tool_name}",
                        "topics": [tool_name.lower(), "documentation"],
                    },
                )

            # 4. Загрузка всех частей файла
            for i, part_path in enumerate(split_files, 1):
                # Адаптируем путь для MCP контейнера
                container_file_path = part_path
                if "\\" in part_path or "docs_parsing" in part_path:
                    filename = os.path.basename(part_path.replace("\\", "/"))
                    container_file_path = f"/app/docs/{filename}"

                print(
                    f"[RAG Service] Загружаем часть {i}/{len(split_files)}: '{container_file_path}'..."
                )
                source_resp = await client.post(
                    f"{NOTEBOOKLM_API_URL}/content/sources",
                    json={
                        "source_type": "file",
                        "file_path": container_file_path,
                        "notebook_url": notebook_url,
                    },
                )
                source_resp.raise_for_status()
                source_data = source_resp.json()

                if not source_data.get("success"):
                    # Игнорируем таймаут обработки, так как файл физически уже загружен
                    if "Timeout waiting for source processing" in source_data.get(
                        "error", ""
                    ):
                        print(
                            f"[RAG Service] Файл {i} загружен, но NotebookLM долго его обрабатывает (это нормально)."
                        )
                    else:
                        raise Exception(
                            f"Ошибка загрузки источника (часть {i}): {source_data.get('error')}"
                        )

            print(f"[RAG Service] Все файлы успешно загружены в RAG!")
            return notebook_id

        except httpx.RequestError as e:
            print(f"[RAG Service] Ошибка сети при обращении к NotebookLM API: {e}")
            raise
        except Exception as e:
            print(f"[RAG Service] Внутренняя ошибка RAG: {e}")
            raise


async def query_global_rag(query: str):
    """
    Архитектура общего окна (LightRAG).
    """
    pass
