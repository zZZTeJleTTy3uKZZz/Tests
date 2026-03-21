from functools import lru_cache
from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

from notebooklm.paths import get_browser_profile_dir, get_storage_path


class AppSettings(BaseSettings):
    """Настройки приложения и интеграции с NotebookLM."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    database_url: str = Field(
        default="sqlite+aiosqlite:///./knowledge_base.db",
        alias="DATABASE_URL",
    )
    notebooklm_home: Path | None = Field(default=None, alias="NOTEBOOKLM_HOME")
    notebooklm_storage_path: Path | None = Field(default=None, alias="NOTEBOOKLM_STORAGE_PATH")
    notebooklm_browser_profile_dir: Path | None = Field(
        default=None,
        alias="NOTEBOOKLM_BROWSER_PROFILE_DIR",
    )
    notebooklm_auto_reauth: bool = Field(default=True, alias="NOTEBOOKLM_AUTO_REAUTH")
    notebooklm_reauth_timeout_seconds: int = Field(
        default=180,
        alias="NOTEBOOKLM_REAUTH_TIMEOUT_SECONDS",
    )
    notebooklm_reauth_headless: bool = Field(
        default=False,
        alias="NOTEBOOKLM_REAUTH_HEADLESS",
    )
    notebooklm_source_wait_timeout_seconds: float = Field(
        default=180.0,
        alias="NOTEBOOKLM_SOURCE_WAIT_TIMEOUT_SECONDS",
    )

    @property
    def resolved_notebooklm_home(self) -> Path:
        if self.notebooklm_home:
            return self.notebooklm_home.expanduser().resolve()
        return get_storage_path().parent

    @property
    def resolved_storage_path(self) -> Path:
        if self.notebooklm_storage_path:
            return self.notebooklm_storage_path.expanduser().resolve()
        return (self.resolved_notebooklm_home / "storage_state.json").resolve()

    @property
    def resolved_browser_profile_dir(self) -> Path:
        if self.notebooklm_browser_profile_dir:
            return self.notebooklm_browser_profile_dir.expanduser().resolve()
        if self.notebooklm_home:
            return (self.resolved_notebooklm_home / "browser_profile").resolve()
        return get_browser_profile_dir().resolve()


@lru_cache
def get_settings() -> AppSettings:
    """Вернуть кэшированный объект настроек."""

    return AppSettings()
