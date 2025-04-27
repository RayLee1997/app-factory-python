from pydantic_settings import BaseSettings, SettingsConfigDict

ENV_FILE = "config/.env.dev"


class Settings(BaseSettings):

    openai_api_key: str

    model_config = SettingsConfigDict(env_file=ENV_FILE, extra="ignore")


settings = Settings()
