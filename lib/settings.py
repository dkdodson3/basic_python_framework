from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(case_sensitive=True)

    url: str = "https://www.abcmouse.com"
    port: str = None
    email_addr: str = "bob@bob.com"
