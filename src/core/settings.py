from pydantic_settings import BaseSettings


class DBConfig(BaseSettings):
    host: str
    port: int
    user: str
    password: str
    name: str

    class Config:
        # env_file = ".env"
        env_prefix = "DB_"
        # env_file_encoding = "utf-8"

    @property
    def dsn(self):
        return f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"


class Settings(BaseSettings):
    db: DBConfig


def get_settings():
    return Settings(db=DBConfig())
