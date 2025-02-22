from typing import Annotated

from litestar import post, status_codes
from litestar.params import Body
from litestar.di import Provide
from litestar.enums import RequestEncodingType


from starters.exc import BusinessException
from starters.auth.service import (
    provide_super_users_service,
    SuperUserService,
    provide_user_service,
    UserService,
)
from starters.auth.model.dto import SuperUserLogin
from starters.auth.model.ec import AuthEC
from starters.auth.jwt import jwt_cookie_auth
from starters.auth.model.entity import User, SuperUser
from starters.config import settings


@post(
    "/admin/token",
    dependencies={"super_user_service": Provide(provide_super_users_service)},
)
async def create_admin_token(
    super_user_service: SuperUserService,
    data: Annotated[SuperUserLogin, Body(media_type=RequestEncodingType.URL_ENCODED)],
) -> None:
    obj = await super_user_service.get_one_or_none(
        super_user_service.model_type.username == data.username
    )
    if obj is None or obj.password != data.password:
        raise BusinessException(AuthEC.LOGIN_FAILED)
    response = jwt_cookie_auth.login(
        identifier=str(obj.user_id),
    )
    response.headers.update({"HX-Redirect": "/admin"})
    return response


@post(
    path="/api/init",
    tags=["初始化"],
    dependencies={
        "user_service": Provide(provide_user_service),
        "super_user_service": Provide(provide_super_users_service),
    },
    status_code=status_codes.HTTP_204_NO_CONTENT,
)
async def init(
    user_service: UserService,
    super_user_service: SuperUserService,
) -> None:
    user_or_none = await user_service.get_one_or_none(User.is_superuser == True)
    if user_or_none is None:
        user = await user_service.create(User(is_superuser=True))
        await super_user_service.create(
            SuperUser(
                user_id=user.id,
                username=settings.auth.superuser,
                password=settings.auth.superuser_pwd,
            )
        )
