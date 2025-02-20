from litestar import Litestar
from litestar.di import Provide
from litestar.openapi import OpenAPIConfig
from core.db import alchemy, provide_limit_offset_pagination
from core.exc import (
    BusinessException,
    ServerException,
    business_exception_handler,
    server_exception_handler,
)
from core.exc.handler import unexpected_error_handler
from core.log import struct_log
from easyai.articles.controller import ArticleController


def create_app() -> Litestar:
    _app = Litestar(
        [ArticleController],
        plugins=[struct_log, alchemy],
        exception_handlers={
            BusinessException: business_exception_handler,
            ServerException: server_exception_handler,
            Exception: unexpected_error_handler,
        },
        dependencies={
            "limit_offset": Provide(
                provide_limit_offset_pagination, sync_to_thread=False
            )
        },
        openapi_config=OpenAPIConfig(title="My API", version="1.0.0"),
    )

    return _app


app = create_app()
