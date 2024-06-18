from pydantic_settings import BaseSettings
from pydantic import AnyHttpUrl, validator
from typing import List, Union

class Settings(BaseSettings):
    PROJECT_NAME: str = "File Generator API Service"
    VERSION: str = "1.0.0"
    API_STR: str = "/api"
    ALLOWED_HOSTS: List[AnyHttpUrl] = ["http://localhost", "http://localhost:8000"]

    # Variables de entorno relacionadas con la base de datos
    DATABASE_URL: str

    @validator("ALLOWED_HOSTS", pre=True)
    def assemble_allowed_hosts(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str):
            return v.split(",")
        return v

    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings()
