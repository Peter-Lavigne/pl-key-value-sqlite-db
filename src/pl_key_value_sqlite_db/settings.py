from pathlib import Path

from pl_mocks_and_fakes import MockInUnitTests, MockReason
from pydantic import Field
from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
        secrets_dir=Path.home() / ".secrets-files",
    )

    # Env-specific config
    key_value_db_path: str = Field(
        validation_alias="KEY_VALUE_DB_PATH", default="~/bin/key_value.db"
    )


@MockInUnitTests(MockReason.UNMITIGATED_SIDE_EFFECT)
def get_settings() -> Settings:
    """Get settings. Raises exception if required settings are missing or invalid."""
    # Required fields are populated from env/.env at runtime; pyright doesn't model that.
    return Settings()  # pyright: ignore[reportCallIssue]
