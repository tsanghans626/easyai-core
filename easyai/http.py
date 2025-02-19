from litestar import Litestar, get, Request
from litestar.plugins.structlog import StructlogPlugin
from litestar.contrib.sqlalchemy.plugins import SQLAlchemyInitPlugin
from core.db import db_config, check_db


@get("/")
async def hello_world(request: Request) -> str:
    return "Hello, world!"


def create_app() -> Litestar:
    _app = Litestar(
        [hello_world],
        plugins=[StructlogPlugin(), SQLAlchemyInitPlugin(db_config)],
        lifespan=[check_db],
    )

    return _app


app = create_app()
