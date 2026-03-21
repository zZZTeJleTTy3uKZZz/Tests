import asyncio
import logging
from pathlib import Path
from typing import Any, Awaitable, Callable, TypeVar

from notebooklm.client import NotebookLMClient
from notebooklm.types import AskResult, Notebook, Source

from app.core.settings import AppSettings, get_settings
from app.services.notebooklm_auth import NotebookLMAuthError, NotebookLMAuthManager

logger = logging.getLogger(__name__)

T = TypeVar("T")


class NotebookLMAdapter:
    """Python-first адаптер над notebooklm-py."""

    def __init__(self, settings: AppSettings | None = None):
        self.settings = settings or get_settings()
        self.auth_manager = NotebookLMAuthManager(self.settings)

    async def health_check(self) -> dict[str, Any]:
        """Проверить auth-state и доступность NotebookLM API."""

        auth_state = await self.auth_manager.get_auth_state()
        result = {
            "success": auth_state.authenticated,
            "authenticated": auth_state.authenticated,
            "storage_path": str(auth_state.storage_path),
            "browser_profile_dir": str(auth_state.browser_profile_dir),
            "notebook_count": None,
            "error": auth_state.error,
        }

        if not auth_state.authenticated:
            return result

        try:
            notebooks = await self.list_notebooks()
            result["notebook_count"] = len(notebooks)
            return result
        except Exception as exc:
            result["success"] = False
            result["error"] = str(exc)
            return result

    async def reauthenticate(
        self,
        timeout_seconds: int | None = None,
        headless: bool | None = None,
    ) -> dict[str, Any]:
        """Переавторизоваться через локальный браузер и обновить storage_state."""

        try:
            state = await self.auth_manager.reauthenticate(
                timeout_seconds=timeout_seconds,
                headless=headless,
            )
            return {
                "success": True,
                "authenticated": state.authenticated,
                "storage_path": str(state.storage_path),
                "browser_profile_dir": str(state.browser_profile_dir),
                "current_url": state.current_url,
                "error": None,
            }
        except Exception as exc:
            return {
                "success": False,
                "authenticated": False,
                "storage_path": str(self.auth_manager.storage_path),
                "browser_profile_dir": str(self.auth_manager.browser_profile_dir),
                "current_url": None,
                "error": str(exc),
            }

    async def list_notebooks(self) -> list[dict[str, Any]]:
        notebooks = await self._run_with_client(lambda client: client.notebooks.list())
        return [self._serialize_notebook(notebook) for notebook in notebooks]

    async def get_or_create_notebook(self, title: str) -> dict[str, Any]:
        async def operation(client: NotebookLMClient) -> Notebook:
            notebooks = await client.notebooks.list()
            for notebook in notebooks:
                if notebook.title == title:
                    return notebook
            return await client.notebooks.create(title)

        notebook = await self._run_with_client(operation)
        return self._serialize_notebook(notebook)

    async def replace_markdown_document(
        self,
        notebook_title: str,
        file_path: str | Path,
        replace_existing_sources: bool = True,
    ) -> dict[str, Any]:
        """Создать или найти блокнот, удалить старые source и залить новый markdown."""

        file_path = Path(file_path).expanduser().resolve()
        if not file_path.exists():
            raise FileNotFoundError(f"Файл документации не найден: {file_path}")

        async def operation(client: NotebookLMClient) -> dict[str, Any]:
            notebooks = await client.notebooks.list()
            notebook = next((nb for nb in notebooks if nb.title == notebook_title), None)
            if notebook is None:
                notebook = await client.notebooks.create(notebook_title)

            sources = await client.sources.list(notebook.id)
            if replace_existing_sources:
                for source in sources:
                    await client.sources.delete(notebook.id, source.id)

            uploaded_source = await client.sources.add_file(
                notebook.id,
                file_path,
                wait=True,
                wait_timeout=self.settings.notebooklm_source_wait_timeout_seconds,
            )

            final_sources = await client.sources.list(notebook.id)
            return {
                "notebook": self._serialize_notebook(notebook),
                "uploaded_source": self._serialize_source(uploaded_source),
                "sources": [self._serialize_source(source) for source in final_sources],
            }

        return await self._run_with_client(operation)

    async def ask_notebook(
        self,
        notebook_id: str,
        question: str,
        source_ids: list[str] | None = None,
        conversation_id: str | None = None,
    ) -> dict[str, Any]:
        async def operation(client: NotebookLMClient) -> dict[str, Any]:
            result = await client.chat.ask(
                notebook_id,
                question,
                source_ids=source_ids,
                conversation_id=conversation_id,
            )
            sources = await client.sources.list(notebook_id)
            source_map = {source.id: source for source in sources}
            return self._serialize_ask_result(notebook_id, result, source_map)

        return await self._run_with_client(operation)

    async def add_text_source(
        self,
        notebook_id: str,
        title: str,
        content: str,
    ) -> dict[str, Any]:
        async def operation(client: NotebookLMClient) -> dict[str, Any]:
            source = await client.sources.add_text(
                notebook_id,
                title=title,
                content=content,
                wait=True,
                wait_timeout=self.settings.notebooklm_source_wait_timeout_seconds,
            )
            return self._serialize_source(source)

        return await self._run_with_client(operation)

    async def ask_multiple_notebooks(
        self,
        notebook_ids: list[str],
        question: str,
    ) -> dict[str, Any]:
        results = await asyncio.gather(
            *(
                self.ask_notebook(notebook_id=notebook_id, question=question)
                for notebook_id in notebook_ids
            )
        )
        merged_answer = "\n\n".join(
            f"[{item['notebook_id']}]\n{item['answer']}" for item in results if item["answer"]
        )
        return {
            "question": question,
            "results": results,
            "merged_answer": merged_answer,
        }

    async def _build_client(self) -> NotebookLMClient:
        try:
            return await NotebookLMClient.from_storage(str(self.auth_manager.storage_path))
        except Exception as exc:
            raise NotebookLMAuthError(str(exc)) from exc

    async def _run_with_client(
        self,
        operation: Callable[[NotebookLMClient], Awaitable[T]],
        *,
        allow_auto_reauth: bool = True,
    ) -> T:
        try:
            client = await self._build_client()
            async with client as opened_client:
                return await operation(opened_client)
        except Exception as exc:
            if allow_auto_reauth and self.settings.notebooklm_auto_reauth and self._is_auth_error(exc):
                logger.warning("Поймали auth-ошибку NotebookLM, пробуем переавторизацию: %s", exc)
                await self.auth_manager.reauthenticate()
                client = await self._build_client()
                async with client as opened_client:
                    return await operation(opened_client)
            raise

    @staticmethod
    def _is_auth_error(exc: Exception) -> bool:
        message = str(exc).lower()
        patterns = (
            "authentication expired",
            "run 'notebooklm login'",
            "redirected to:",
            "not logged in",
        )
        return isinstance(exc, (FileNotFoundError, NotebookLMAuthError)) or any(
            pattern in message for pattern in patterns
        )

    @staticmethod
    def _serialize_notebook(notebook: Notebook) -> dict[str, Any]:
        return {
            "id": notebook.id,
            "title": notebook.title,
            "created_at": notebook.created_at.isoformat() if notebook.created_at else None,
            "sources_count": notebook.sources_count,
            "is_owner": notebook.is_owner,
        }

    @staticmethod
    def _serialize_source(source: Source) -> dict[str, Any]:
        return {
            "id": source.id,
            "title": source.title,
            "url": source.url,
            "kind": source.kind.value if hasattr(source.kind, "value") else str(source.kind),
            "status": source.status,
            "created_at": source.created_at.isoformat() if source.created_at else None,
        }

    @staticmethod
    def _serialize_ask_result(
        notebook_id: str,
        result: AskResult,
        source_map: dict[str, Source],
    ) -> dict[str, Any]:
        references = []
        for reference in result.references:
            source = source_map.get(reference.source_id)
            references.append(
                {
                    "source_id": reference.source_id,
                    "citation_number": reference.citation_number,
                    "cited_text": reference.cited_text,
                    "source_title": source.title if source else None,
                    "source_url": source.url if source else None,
                }
            )

        return {
            "notebook_id": notebook_id,
            "answer": result.answer,
            "conversation_id": result.conversation_id,
            "turn_number": result.turn_number,
            "is_follow_up": result.is_follow_up,
            "references": references,
        }


_adapter_instance: NotebookLMAdapter | None = None


def get_notebooklm_adapter() -> NotebookLMAdapter:
    """Вернуть singleton-адаптер NotebookLM."""

    global _adapter_instance
    if _adapter_instance is None:
        _adapter_instance = NotebookLMAdapter()
    return _adapter_instance
