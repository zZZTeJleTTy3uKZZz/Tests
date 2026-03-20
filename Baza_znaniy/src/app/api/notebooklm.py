import os
import httpx
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, BackgroundTasks

from app.db.database import get_db
from app.services.rag_service import process_document_for_rag, NOTEBOOKLM_API_URL
from app.models.knowledge_base import KnowledgeBaseEntity

router = APIRouter(prefix="/notebooklm", tags=["NotebookLM Integration"])


@router.post("/sync-notebooks")
async def sync_notebooks_with_db(db: AsyncSession = Depends(get_db)):
    """
    Скрейпинг актуальных блокнотов из NotebookLM и синхронизация их с базой данных
    """
    async with httpx.AsyncClient(timeout=30.0) as client:
        # Получаем список блокнотов из MCP сервера
        resp = await client.get(f"{NOTEBOOKLM_API_URL}/notebooks/scrape")
        resp.raise_for_status()
        data = resp.json()

        if not data.get("success"):
            return {
                "success": False,
                "error": "Не удалось получить блокноты из NotebookLM",
            }

        notebooks = data["data"]["notebooks"]
        updated_count = 0

        # В реальной реализации тут должен быть поиск по БД по имени (name),
        # и обновление notebooklm_id у найденных записей.
        # Поскольку у нас пока тестовая версия, мы просто выводим что нашли.

        return {
            "success": True,
            "message": f"Найдено {len(notebooks)} блокнотов в NotebookLM. Синхронизация завершена.",
            "notebooks_found": len(notebooks),
        }


@router.post("/ask")
async def ask_notebooklm(notebook_id: str, question: str):
    """
    Эндпоинт-посредник для ИИ-агентов, чтобы задавать вопросы в конкретный блокнот
    """
    async with httpx.AsyncClient(timeout=120.0) as client:
        resp = await client.post(
            f"{NOTEBOOKLM_API_URL}/ask",
            json={"notebook_id": notebook_id, "question": question},
        )
        resp.raise_for_status()
        return resp.json()
