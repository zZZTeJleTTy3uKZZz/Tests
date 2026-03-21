# База знаний технической документации API

Это Backend-система для централизованного учета, управления и взаимодействия со спарсенными техническими документациями.
Включает CRUD API и интеграции с RAG системами (NotebookLM, LightRAG).

## Интеграция с NotebookLM через `notebooklm-py`

Платформа интегрируется с Google NotebookLM напрямую через Python-библиотеку `notebooklm-py`, без промежуточного `MCP`-HTTP сервера.
Старый vendored `notebooklm-mcp` удалён из репозитория, чтобы в проекте оставался один поддерживаемый способ интеграции.

Когда документ в БД переходит в статус `Загружается в RAG`, FastAPI:
1. Находит или создаёт блокнот в NotebookLM.
2. При необходимости переавторизуется через локальный браузер.
3. Удаляет старые `source` внутри целевого блокнота.
4. Загружает актуальный `.md` файл как новый источник.
5. Сохраняет `notebooklm_id` в БД.

> ⚠️ **ВАЖНО**: Для live-режима на ноутбуке нужен валидный `storage_state.json`. Его можно получить командой `notebooklm login` или встроенным эндпоинтом `/api/v1/notebooklm/re-auth`.

### Сервисные эндпоинты NotebookLM

- `GET /api/v1/notebooklm/health` — проверить, валидна ли текущая авторизация и доступен ли список блокнотов.
- `POST /api/v1/notebooklm/re-auth` — открыть локальный браузер, дождаться логина и сохранить новый `storage_state.json`.
- `GET /api/v1/notebooklm/notebooks` — получить список блокнотов.
- `POST /api/v1/notebooklm/ask` — задать вопрос одному блокноту.
- `POST /api/v1/notebooklm/ask-batch` — отправить один вопрос в несколько блокнотов и агрегировать ответы.

## Инструкция по запуску с помощью Docker

Убедитесь, что у вас установлен `docker` и `docker-compose`.

```bash
cd "База знаний технической документации/src"
docker-compose up -d --build
```

**Доступные сервисы:**
- **FastAPI Бэкенд**: http://localhost:8000 (Документация Swagger: http://localhost:8000/docs)

## Инструкция по локальному запуску (без Docker)

Вам потребуется установленный Python 3.11+ и пакетный менеджер `uv`.

```bash
cd src/
uv sync
uv run alembic upgrade head
uv run uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### Авторизация NotebookLM для локального режима

```bash
cd src/
uv run notebooklm login
```

Либо используйте API:

```bash
POST http://localhost:8000/api/v1/notebooklm/re-auth
```

## Архитектура и PRD

Подробное техническое задание (PRD) и описание архитектуры находится в папке `docs/03_PRD/PRD.md`.
