from litestar import Litestar
from litestar.plugins.structlog import StructlogPlugin
from litestar.contrib.sqlalchemy.plugins import SQLAlchemyInitPlugin
from core.db import db_config
from core.exc import BusinessException, ServerException, business_exception_handler, server_exception_handler


def create_app() -> Litestar:
    _app = Litestar(
        plugins=[StructlogPlugin(), SQLAlchemyInitPlugin(db_config)],
        exception_handlers={
            BusinessException: business_exception_handler,
            ServerException: server_exception_handler,
        },
    )

    return _app


app = create_app()
