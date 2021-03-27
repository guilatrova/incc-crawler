from pydantic import BaseSettings


class Settings(BaseSettings):
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

    BOT_TOKEN: str
    CHAT_ID: str
    CHAT_PARSE_MODE: str = "MarkdownV2"  # or HTML
    TRIGGER_URL: str = ""


settings = Settings()
