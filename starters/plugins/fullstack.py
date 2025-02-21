from pathlib import Path

from litestar.exceptions import NotFoundException
from litestar.config.app import AppConfig
from litestar.di import Provide
from litestar.openapi import OpenAPIConfig
from litestar.plugins import InitPluginProtocol
from litestar.plugins.structlog import StructlogPlugin
from litestar.plugins.htmx import HTMXPlugin
from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.template.config import TemplateConfig
from litestar.static_files import create_static_files_router

from starters.exc import (
    BusinessException,
    ServerException,
    business_exception_handler,
    server_exception_handler,
    unexpected_error_handler,
    notfound_handler,
)
from starters.db import alchemy, provide_limit_offset_pagination
from starters.auth import jwt_cookie_auth, login, init, login_view


class FullstackStarterPlugin(InitPluginProtocol):
    def on_app_init(self, app_config: AppConfig) -> AppConfig:
        app_config.route_handlers.extend(
            [create_static_files_router(path="/", directories=["assets"]), login, init, login_view]
        )
        app_config.plugins.extend([StructlogPlugin(), alchemy, HTMXPlugin()])

        app_config.template_config = TemplateConfig(
            directory=Path("templates"),
            engine=JinjaTemplateEngine,
        )
        app_config.exception_handlers = {
            BusinessException: business_exception_handler,
            NotFoundException: notfound_handler,
            ServerException: server_exception_handler,
            Exception: unexpected_error_handler,
        }
        app_config.dependencies = {
            "limit_offset": Provide(
                provide_limit_offset_pagination, sync_to_thread=False
            )
        }
        app_config.openapi_config = OpenAPIConfig(title="My API", version="1.0.0")

        jwt_cookie_auth.on_app_init(app_config)
        return app_config
