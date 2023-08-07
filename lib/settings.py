from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(case_sensitive=True, env_file="../.env")

    url: str = "https://www.abcmouse.com"
    port: str = ""
    email_addr: str = "bob@bob.com"


@lru_cache()
def get_settings() -> Settings:
    return Settings()