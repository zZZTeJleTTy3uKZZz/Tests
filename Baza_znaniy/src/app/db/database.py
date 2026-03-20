import os
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base

SQLALCHEMY_DATABASE_URL = os.getenv(
    "DATABASE_URL", "sqlite+aiosqlite:///./knowledge_base.db"
)

# Для SQLite нужно добавлять параметр check_same_thread
connect_args = (
    {"check_same_thread": False} if "sqlite" in SQLALCHEMY_DATABASE_URL else {}
)

engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL, connect_args=connect_args, echo=True
)

AsyncSessionLocal = async_sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

Base = declarative_base()


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
