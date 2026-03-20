from fastapi import FastAPI
from app.api import docs
from app.api import notebooklm

app = FastAPI(
    title="Knowledge Base API",
    description="API для управления базой знаний спарсенных технических документаций",
    version="1.0.0",
)

app.include_router(docs.router)
app.include_router(notebooklm.router)


@app.get("/")
def read_root():
    return {
        "message": "Добро пожаловать в API Базы Знаний. Перейдите на /docs для просмотра документации."
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
