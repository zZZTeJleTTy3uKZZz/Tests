from sqlalchemy import Column, String, Integer, DateTime, Enum, Text
import enum
from datetime import datetime, timezone
import uuid
from app.db.database import Base


class DocStatus(str, enum.Enum):
    PLANNED = "Планируется"
    PARSER_CREATION = "Создание парсера"
    PARSING = "Парсится"
    LOADING_TO_RAG = "Загружается в RAG"
    ACTUAL_VERSION = "Актуальная версия"
    OUTDATED_VERSION = "Устаревшая версия"


class KnowledgeBaseEntity(Base):
    __tablename__ = "knowledge_base"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False, index=True)
    status = Column(Enum(DocStatus), default=DocStatus.PLANNED, nullable=False)
    version = Column(String, nullable=False)
    direction = Column(
        String, nullable=False
    )  # ИИ агенты, разработка, маркетинг и т.д.
    category = Column(
        String, nullable=False
    )  # Язык программирования, сервис, приложение и т.д.
    doc_type = Column(
        String, nullable=False
    )  # Техническая документация, инструкции, курсы и т.д.
    notebooklm_id = Column(String, nullable=True)  # ID блокнота
    source_url = Column(String, nullable=True)
    local_path = Column(String, nullable=True)

    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )
