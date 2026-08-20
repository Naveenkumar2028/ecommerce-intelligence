import os
from pydantic import BaseModel

class Settings(BaseModel):
    PROJECT_NAME: str = "E-Commerce Intelligence Platform"
    VERSION: str = "2.0.0"
    API_V1_STR: str = "/api"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./ecommerce.db")
    CORS_ORIGINS: list[str] = ["*"]
    DEFAULT_DATE_RANGE_DAYS: int = 30

settings = Settings()
