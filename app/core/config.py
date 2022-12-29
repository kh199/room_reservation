from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Бронирование переговорок'
    app_description: str = 'Позволяет сотрудникам резервировать переговорки'
    database_url: str

    class Config:
        env_file = '.env'

settings = Settings()
