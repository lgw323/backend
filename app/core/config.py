import secrets
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyHttpUrl, PostgresDsn, validator
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "CASTMATCH"
    API_V1_STR: str = "/api/v1"
    
    # 보안 설정
    SECRET_KEY: str = "CHANGE_ME_PLEASE_IN_PRODUCTION" # secrets.token_urlsafe(32) 권장
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8일
    
    # CORS 설정
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    # Database
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "castmatch"
    POSTGRES_PORT: str = "5432"
    
    # Async DB URI
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> Optional[str]:
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        
    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings()
