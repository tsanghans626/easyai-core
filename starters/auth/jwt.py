from typing import Any

from litestar.connection import ASGIConnection
from litestar.security.jwt import JWTCookieAuth, Token
from starters.auth.service import UserService
from starters.auth.model.entity import User
from starters.config import settings


async def retrieve_user_handler(
    token: Token,
    connection: "ASGIConnection[Any, Any, Any, Any]",
    user_service: UserService,
) -> User | None:
    user_id = int(token.sub)

    return await user_service.get_one_or_none(User.id == user_id)


jwt_cookie_auth = JWTCookieAuth[User](
    retrieve_user_handler=retrieve_user_handler,
    token_secret=settings.auth.secret,
    exclude_http_methods=["GET"],
    exclude=["/api/login"]
)
