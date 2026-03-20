from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime
from app.models.knowledge_base import DocStatus


class KnowledgeBaseBase(BaseModel):
    name: str = Field(..., title="Название инструмента")
    status: DocStatus = Field(default=DocStatus.PLANNED, title="Статус")
    version: str = Field(..., title="Версия документации")
    direction: str = Field(..., title="Направление")
    category: str = Field(..., title="Категория")
    doc_type: str = Field(..., title="Тип")
    notebooklm_id: Optional[str] = Field(None, title="ID блокнота в NotebookLM")
    source_url: Optional[str] = Field(None, title="Ссылка на источник")
    local_path: Optional[str] = Field(None, title="Локальный путь к markdown")


class KnowledgeBaseCreate(KnowledgeBaseBase):
    pass


class KnowledgeBaseUpdate(BaseModel):
    name: Optional[str] = None
    status: Optional[DocStatus] = None
    version: Optional[str] = None
    direction: Optional[str] = None
    category: Optional[str] = None
    doc_type: Optional[str] = None
    notebooklm_id: Optional[str] = None
    source_url: Optional[str] = None
    local_path: Optional[str] = None


class KnowledgeBaseResponse(KnowledgeBaseBase):
    id: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
