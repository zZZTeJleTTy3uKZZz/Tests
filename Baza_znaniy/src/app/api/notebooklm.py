from fastapi import APIRouter, Depends, HTTPException

from app.schemas.notebooklm import (
    NotebookLMAskRequest,
    NotebookLMAskResponse,
    NotebookLMBatchAskRequest,
    NotebookLMBatchAskResponse,
    NotebookLMHealthResponse,
    NotebookLMNotebookResponse,
    NotebookLMReauthRequest,
    NotebookLMReauthResponse,
)
from app.services.notebooklm_adapter import NotebookLMAdapter, get_notebooklm_adapter

router = APIRouter(prefix="/api/v1/notebooklm", tags=["NotebookLM"])


def _get_adapter() -> NotebookLMAdapter:
    return get_notebooklm_adapter()


@router.get("/health", response_model=NotebookLMHealthResponse)
async def notebooklm_health(adapter: NotebookLMAdapter = Depends(_get_adapter)):
    return await adapter.health_check()


@router.post("/re-auth", response_model=NotebookLMReauthResponse)
async def notebooklm_reauth(
    request: NotebookLMReauthRequest,
    adapter: NotebookLMAdapter = Depends(_get_adapter),
):
    result = await adapter.reauthenticate(
        timeout_seconds=request.timeout_seconds,
        headless=request.headless,
    )
    if not result["success"]:
        raise HTTPException(status_code=500, detail=result["error"])
    return result


@router.get("/notebooks", response_model=list[NotebookLMNotebookResponse])
async def notebooklm_list_notebooks(adapter: NotebookLMAdapter = Depends(_get_adapter)):
    return await adapter.list_notebooks()


@router.post("/ask", response_model=NotebookLMAskResponse)
async def ask_notebooklm(
    request: NotebookLMAskRequest,
    adapter: NotebookLMAdapter = Depends(_get_adapter),
):
    try:
        return await adapter.ask_notebook(
            notebook_id=request.notebook_id,
            question=request.question,
            source_ids=request.source_ids,
            conversation_id=request.conversation_id,
        )
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc


@router.post("/ask-batch", response_model=NotebookLMBatchAskResponse)
async def ask_notebooklm_batch(
    request: NotebookLMBatchAskRequest,
    adapter: NotebookLMAdapter = Depends(_get_adapter),
):
    try:
        return await adapter.ask_multiple_notebooks(
            notebook_ids=request.notebook_ids,
            question=request.question,
        )
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc
