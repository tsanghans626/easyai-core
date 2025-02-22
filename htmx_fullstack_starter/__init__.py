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

from htmx_fullstack_starter.exc import (
    BusinessException,
    business_exception_handler,
    unexpected_error_handler,
    notfound_handler,
)
from htmx_fullstack_starter.db import alchemy, provide_limit_offset_pagination
from htmx_fullstack_starter.auth import (
    init,
    create_admin_token,
    get_admin_login_view,
    jwt_cookie_auth,
)
from htmx_fullstack_starter.admin import get_admin_view
from htmx_fullstack_starter.config import settings


__all__ = ["FullstackStarterPlugin"]


class FullstackStarterPlugin(InitPluginProtocol):
    def on_app_init(self, app_config: AppConfig) -> AppConfig:
        app_config.route_handlers.extend(
            [
                create_static_files_router(path="/static", directories=["assets"]),
                create_admin_token,
                init,
                get_admin_login_view,
                get_admin_view
            ]
        )
        app_config.plugins.extend([StructlogPlugin(), alchemy, HTMXPlugin()])
        app_config.opt.update({"secret": settings.auth.secret})

        app_config.template_config = TemplateConfig(
            directory=Path("templates"),
            engine=JinjaTemplateEngine,
        )
        app_config.exception_handlers = {
            BusinessException: business_exception_handler,
            NotFoundException: notfound_handler,
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


