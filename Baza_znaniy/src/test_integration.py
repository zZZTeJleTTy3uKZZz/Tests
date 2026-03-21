import asyncio

from app.db.database import AsyncSessionLocal
from app.models.knowledge_base import KnowledgeBaseEntity, DocStatus
from app.services.rag_service import process_document_for_rag
from sqlalchemy import select


async def main():
    print("--- 1. Создаем тестовую запись в БД ---")
    tool_name = "Opencode_Prod"
    file_path = "../../docs_parsing/test_opencode.md"

    async with AsyncSessionLocal() as session:
        # Проверим, есть ли уже такая запись
        stmt = select(KnowledgeBaseEntity).where(KnowledgeBaseEntity.name == tool_name)
        result = await session.execute(stmt)
        doc = result.scalar_one_or_none()

        if not doc:
            doc = KnowledgeBaseEntity(
                name=tool_name,
                status=DocStatus.LOADING_TO_RAG,
                version="latest",
                direction="ИИ агенты",
                category="Фреймворк",
                doc_type="Техническая документация",
                local_path=file_path,
            )
            session.add(doc)
            await session.commit()
            await session.refresh(doc)
            print(f"✅ Создана новая запись: ID={doc.id}, Name={doc.name}")
        else:
            print(f"✅ Запись уже существует: ID={doc.id}, Name={doc.name}")
            doc.status = DocStatus.LOADING_TO_RAG
            doc.local_path = file_path
            await session.commit()

        doc_id = doc.id

    print("\n--- 2. Запускаем интеграцию с NotebookLM ---")
    try:
        notebook_id = await process_document_for_rag(
            doc_id=doc_id, file_path=file_path, tool_name=tool_name
        )
        print(f"✅ Успешно загружено! Получен notebook_id: {notebook_id}")

        print("\n--- 3. Обновляем статус в БД ---")
        async with AsyncSessionLocal() as session:
            stmt = select(KnowledgeBaseEntity).where(KnowledgeBaseEntity.id == doc_id)
            result = await session.execute(stmt)
            doc = result.scalar_one_or_none()
            doc.notebooklm_id = notebook_id
            doc.status = DocStatus.ACTUAL_VERSION
            await session.commit()
            print("✅ Запись обновлена. RAG Интеграция полностью завершена.")

    except Exception as e:
        print(f"❌ Ошибка в процессе RAG интеграции: {e}")


if __name__ == "__main__":
    asyncio.run(main())
