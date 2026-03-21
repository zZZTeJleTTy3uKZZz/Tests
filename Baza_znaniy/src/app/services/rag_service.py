from pathlib import Path

from app.services.notebooklm_adapter import get_notebooklm_adapter


async def process_document_for_rag(doc_id: str, file_path: str, tool_name: str) -> str:
    """
    Интеграция с NotebookLM через notebooklm-py.

    Создаёт или находит блокнот по имени инструмента, заменяет текущие
    sources и загружает актуальный markdown-файл как основной источник.
    """
    adapter = get_notebooklm_adapter()
    local_file_path = Path(file_path).expanduser()

    if not local_file_path.exists() and "/app/docs" in str(local_file_path):
        local_file_path = Path(str(local_file_path).replace("/app/docs", "../../docs_parsing"))

    result = await adapter.replace_markdown_document(
        notebook_title=tool_name,
        file_path=local_file_path,
        replace_existing_sources=True,
    )
    return result["notebook"]["id"]


async def query_global_rag(query: str):
    """
    Архитектура общего окна (LightRAG).
    """
    pass
