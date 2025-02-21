from typing import Any


from litestar.connection import ASGIConnection
from litestar.security.jwt import JWTAuth, Token
from starters.auth.service import UserService, provide_user_service
from starters.auth.model.entity import User
from starters.config import settings


async def retrieve_user_handler(
    token: Token,
    connection: "ASGIConnection[Any, Any, Any, Any]",
    auth_service: UserService,
) -> User | None:
    user_id = int(token.sub)

    return await auth_service.get_one_or_none(User.id == user_id)


jwt_auth = JWTAuth[User](
    retrieve_user_handler=retrieve_user_handler,
    token_secret=settings.auth.secret,
    # we are specifying which endpoints should be excluded from authentication. In this case the login endpoint
    # and our openAPI docs.
    exclude=["/login", "/schema"],
    dependencies={"auth_service": provide_user_service},
)
