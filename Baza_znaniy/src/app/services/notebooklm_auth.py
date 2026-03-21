import asyncio
import logging
import sys
import time
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator

from notebooklm.auth import AuthTokens

from app.core.settings import AppSettings, get_settings

logger = logging.getLogger(__name__)

NOTEBOOKLM_URL = "https://notebooklm.google.com/"
GOOGLE_ACCOUNTS_URL = "https://accounts.google.com/"
NOTEBOOKLM_HOST = "notebooklm.google.com"


class NotebookLMAuthError(RuntimeError):
    """Базовая ошибка аутентификации NotebookLM."""


class NotebookLMReauthTimeoutError(NotebookLMAuthError):
    """Не удалось автоматически дождаться новой сессии NotebookLM."""


@dataclass
class NotebookLMAuthState:
    authenticated: bool
    storage_path: Path
    browser_profile_dir: Path
    error: str | None = None
    current_url: str | None = None


@contextmanager
def _windows_playwright_event_loop() -> Iterator[None]:
    """Временно вернуть стандартный event loop policy для Playwright на Windows."""

    if sys.platform != "win32":
        yield
        return

    original_policy = asyncio.get_event_loop_policy()
    asyncio.set_event_loop_policy(asyncio.DefaultEventLoopPolicy())
    try:
        yield
    finally:
        asyncio.set_event_loop_policy(original_policy)


class NotebookLMAuthManager:
    """Управляет auth-state для NotebookLM без MCP-прокси."""

    def __init__(self, settings: AppSettings | None = None):
        self.settings = settings or get_settings()

    @property
    def storage_path(self) -> Path:
        return self.settings.resolved_storage_path

    @property
    def browser_profile_dir(self) -> Path:
        return self.settings.resolved_browser_profile_dir

    async def get_auth_tokens(self) -> AuthTokens:
        """Получить валидные токены из storage_state.json."""

        return await AuthTokens.from_storage(self.storage_path)

    async def get_auth_state(self) -> NotebookLMAuthState:
        """Проверить, валиден ли текущий auth-state."""

        try:
            await self.get_auth_tokens()
            authenticated = True
            error = None
        except Exception as exc:
            authenticated = False
            error = str(exc)

        return NotebookLMAuthState(
            authenticated=authenticated,
            storage_path=self.storage_path,
            browser_profile_dir=self.browser_profile_dir,
            error=error,
        )

    async def reauthenticate(
        self,
        timeout_seconds: int | None = None,
        headless: bool | None = None,
    ) -> NotebookLMAuthState:
        """Открыть браузер, дождаться NotebookLM и сохранить свежий storage_state."""

        timeout_seconds = timeout_seconds or self.settings.notebooklm_reauth_timeout_seconds
        headless = (
            self.settings.notebooklm_reauth_headless if headless is None else headless
        )

        result = await asyncio.to_thread(
            self._reauthenticate_sync,
            timeout_seconds,
            headless,
        )

        await self.get_auth_tokens()
        return result

    def _reauthenticate_sync(
        self,
        timeout_seconds: int,
        headless: bool,
    ) -> NotebookLMAuthState:
        """Синхронный браузерный цикл re-auth в отдельном потоке."""

        try:
            from playwright.sync_api import sync_playwright
        except ImportError as exc:
            raise NotebookLMAuthError(
                "Playwright не установлен. Выполните `uv run playwright install chromium`."
            ) from exc

        self.storage_path.parent.mkdir(parents=True, exist_ok=True)
        self.browser_profile_dir.mkdir(parents=True, exist_ok=True)

        logger.info(
            "Запускаем переавторизацию NotebookLM. storage=%s profile=%s",
            self.storage_path,
            self.browser_profile_dir,
        )

        with _windows_playwright_event_loop(), sync_playwright() as playwright:
            context = playwright.chromium.launch_persistent_context(
                user_data_dir=str(self.browser_profile_dir),
                headless=headless,
                args=[
                    "--disable-blink-features=AutomationControlled",
                    "--password-store=basic",
                ],
                ignore_default_args=["--enable-automation"],
            )

            try:
                page = context.pages[0] if context.pages else context.new_page()
                self._safe_goto(page, NOTEBOOKLM_URL, timeout_ms=60_000)

                deadline = time.monotonic() + timeout_seconds
                last_url = page.url

                while time.monotonic() < deadline:
                    last_url = page.url
                    cookie_names = {cookie["name"] for cookie in context.cookies()}
                    has_google_session = "SID" in cookie_names

                    if NOTEBOOKLM_HOST in last_url and has_google_session:
                        page.wait_for_timeout(3_000)
                        self._safe_goto(page, GOOGLE_ACCOUNTS_URL, timeout_ms=30_000)
                        self._safe_goto(page, NOTEBOOKLM_URL, timeout_ms=30_000)
                        last_url = page.url

                        if NOTEBOOKLM_HOST in last_url:
                            context.storage_state(path=str(self.storage_path))
                            try:
                                self.storage_path.chmod(0o600)
                            except OSError:
                                logger.debug(
                                    "Не удалось изменить права на %s на Windows",
                                    self.storage_path,
                                )

                            logger.info("storage_state обновлён: %s", self.storage_path)
                            return NotebookLMAuthState(
                                authenticated=True,
                                storage_path=self.storage_path,
                                browser_profile_dir=self.browser_profile_dir,
                                current_url=last_url,
                            )

                    if NOTEBOOKLM_HOST in last_url and not has_google_session:
                        logger.info(
                            "NotebookLM открыт, но SID ещё не появился. Ждём завершения ручного логина."
                        )

                    page.wait_for_timeout(1_000)

                raise NotebookLMReauthTimeoutError(
                    "Не удалось дождаться страницы NotebookLM. "
                    "Если Google запросил ручной логин, завершите его в открывшемся окне."
                )
            finally:
                context.close()

    @staticmethod
    def _safe_goto(page, url: str, timeout_ms: int) -> None:
        """Перейти на страницу и не падать, если загрузка дотянулась до timeout."""

        try:
            page.goto(url, wait_until="domcontentloaded", timeout=timeout_ms)
        except Exception as exc:
            logger.warning("Navigation timeout for %s: %s", url, exc)
