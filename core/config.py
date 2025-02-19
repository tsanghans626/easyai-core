from typing import Literal

import msgspec
from sqlalchemy import URL


class DbSettings(msgspec.Struct):
    host: str
    port: int
    user: str
    pwd: str
    schema: str
    pool_size: int = 1024
    max_overflow: int = 1024
    echo: bool = False
    pool_pre_ping: bool = True
    pool_recycle: int = 1800

    @property
    def sqlalchemy_url(self) -> URL:
        return URL.create(
            "mysql+asyncmy",
            username=self.user,
            password=self.pwd,
            host=self.host,
            port=self.port,
            database=self.schema,
        )


class Settings(msgspec.Struct):
    db: DbSettings
    env: Literal["production", "test", "development"] = "production"


def get_settings() -> Settings:
    with open("application.yaml", mode="r") as f:
        content = f.read()
        _settings = msgspec.yaml.decode(content, type=Settings)
    return _settings


settings = get_settings()
