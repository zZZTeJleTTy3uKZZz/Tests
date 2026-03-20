from fastapi import APIRouter, Depends, HTTPException, status, BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete
from typing import List, Optional

from app.db.database import get_db
from app.models.knowledge_base import KnowledgeBaseEntity, DocStatus
from app.schemas.knowledge_base import (
    KnowledgeBaseCreate,
    KnowledgeBaseResponse,
    KnowledgeBaseUpdate,
)
from app.services.rag_service import process_document_for_rag

router = APIRouter(prefix="/api/v1/docs", tags=["Documentation"])


async def background_rag_upload(
    doc_id: str, file_path: str, tool_name: str, db_session: AsyncSession
):
    """Фоновая задача для загрузки документа в NotebookLM через MCP сервер"""
    try:
        notebook_id = await process_document_for_rag(doc_id, file_path, tool_name)

        # Обновляем БД: сохраняем ID блокнота и статус
        query = select(KnowledgeBaseEntity).where(KnowledgeBaseEntity.id == doc_id)
        result = await db_session.execute(query)
        db_doc = result.scalar_one_or_none()

        if db_doc:
            db_doc.notebooklm_id = notebook_id
            db_doc.status = DocStatus.ACTUAL_VERSION
            await db_session.commit()

    except Exception as e:
        print(f"Ошибка при загрузке RAG для документа {doc_id}: {e}")
        # Можно поставить статус "Ошибка загрузки в RAG", если расширить enum


@router.post(
    "/", response_model=KnowledgeBaseResponse, status_code=status.HTTP_201_CREATED
)
async def create_doc(
    doc_in: KnowledgeBaseCreate,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db),
):
    db_doc = KnowledgeBaseEntity(**doc_in.model_dump())
    db.add(db_doc)
    await db.commit()
    await db.refresh(db_doc)

    # Если мы создали документ сразу со статусом загрузки, запускаем фоновую задачу
    if db_doc.status == DocStatus.LOADING_TO_RAG and db_doc.local_path:
        # Для фоновых задач с алхимией лучше создавать новую сессию
        # Для простоты здесь передается текущая, но в проде нужно использовать AsyncSessionLocal
        background_tasks.add_task(
            background_rag_upload, db_doc.id, db_doc.local_path, db_doc.name, db
        )

    return db_doc


@router.get("/", response_model=List[KnowledgeBaseResponse])
async def read_docs(
    skip: int = 0,
    limit: int = 100,
    doc_status: Optional[DocStatus] = None,
    category: Optional[str] = None,
    direction: Optional[str] = None,
    db: AsyncSession = Depends(get_db),
):
    query = select(KnowledgeBaseEntity)

    if doc_status:
        query = query.where(KnowledgeBaseEntity.status == doc_status)
    if category:
        query = query.where(KnowledgeBaseEntity.category == category)
    if direction:
        query = query.where(KnowledgeBaseEntity.direction == direction)

    query = query.offset(skip).limit(limit)
    result = await db.execute(query)
    return result.scalars().all()


@router.get("/{doc_id}", response_model=KnowledgeBaseResponse)
async def read_doc(doc_id: str, db: AsyncSession = Depends(get_db)):
    query = select(KnowledgeBaseEntity).where(KnowledgeBaseEntity.id == doc_id)
    result = await db.execute(query)
    db_doc = result.scalar_one_or_none()

    if not db_doc:
        raise HTTPException(status_code=404, detail="Документация не найдена")
    return db_doc


@router.patch("/{doc_id}", response_model=KnowledgeBaseResponse)
async def update_doc(
    doc_id: str, doc_in: KnowledgeBaseUpdate, db: AsyncSession = Depends(get_db)
):
    query = select(KnowledgeBaseEntity).where(KnowledgeBaseEntity.id == doc_id)
    result = await db.execute(query)
    db_doc = result.scalar_one_or_none()

    if not db_doc:
        raise HTTPException(status_code=404, detail="Документация не найдена")

    update_data = doc_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_doc, field, value)

    await db.commit()
    await db.refresh(db_doc)
    return db_doc


@router.delete("/{doc_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_doc(doc_id: str, db: AsyncSession = Depends(get_db)):
    query = select(KnowledgeBaseEntity).where(KnowledgeBaseEntity.id == doc_id)
    result = await db.execute(query)
    db_doc = result.scalar_one_or_none()

    if not db_doc:
        raise HTTPException(status_code=404, detail="Документация не найдена")

    await db.delete(db_doc)
    await db.commit()
    return None
