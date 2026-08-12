"""Application configuration using Pydantic Settings."""
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # Application
    app_name: str = "azure-agentic-ai-platform"
    app_env: str = "development"
    app_host: str = "0.0.0.0"
    app_port: int = 8000
    log_level: str = "INFO"

    # CORS
    allowed_origins: str = "http://localhost:3000,http://localhost:8000"

    # Azure OpenAI (placeholders — populated in feature branches)
    azure_openai_endpoint: str = ""
    azure_openai_api_key: str = ""
    azure_openai_deployment: str = ""
    azure_openai_api_version: str = "2024-02-01"

    @property
    def cors_origins(self) -> list[str]:
        """Return CORS origins as a list."""
        return [origin.strip() for origin in self.allowed_origins.split(",")]


settings = Settings()
