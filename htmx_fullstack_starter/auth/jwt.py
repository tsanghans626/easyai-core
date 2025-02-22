from typing import Any

from litestar.connection import ASGIConnection
from litestar.exceptions import NotAuthorizedException
from litestar.security.jwt import JWTCookieAuth, Token
from litestar.handlers.base import BaseRouteHandler
from litestar.connection import ASGIConnection
from htmx_fullstack_starter.auth.model.entity import User
from htmx_fullstack_starter.config import settings


async def retrieve_user_handler(
    token: Token,
    connection: "ASGIConnection[Any, Any, Any, Any]",
) -> User | None:
    return User(id=token.sub)


jwt_cookie_auth = JWTCookieAuth[User](
    retrieve_user_handler=retrieve_user_handler,
    token_secret=settings.auth.secret,
    exclude=["/admin/login", "/admin/token", "/static"],
)
