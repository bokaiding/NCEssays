from pydantic_settings import BaseSettings
from typing import Literal


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    # LLM Configuration
    llm_api_key: str
    llm_provider: Literal["openai", "anthropic", "ollama"] = "openai"
    
    # Database
    database_url: str
    
    # Rate Limiting
    rate_limit_per_minute: int = 10
    
    # Optional: Ollama Configuration
    ollama_base_url: str = "http://localhost:11434"
    ollama_model: str = "llama2"
    
    # Optional: API Base URLs
    openai_api_base: str = "https://api.openai.com/v1"
    anthropic_api_base: str = "https://api.anthropic.com"
    
    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
