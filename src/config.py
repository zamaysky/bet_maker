from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_NAME: str
    DB_PASSWORD: str

    @property
    def db_url_asyncpg(self) -> str:
        return (
            f'postgresql+asyncpg://'
            f'{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'
        )

    model_config = SettingsConfigDict(env_file='.env', extra='allow')


settings = Settings()
