from pydantic_settings import BaseSettings

ENV_FILE = ".env.dev"


class Settings(BaseSettings):
    openai_api_key: str

    class Config:
        env_file = ENV_FILE


settings = Settings()
