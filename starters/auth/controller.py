from typing import Annotated
from litestar import post
from litestar.di import Provide
from litestar.enums import RequestEncodingType
from litestar.params import Body

from starters.auth import jwt_auth
from starters.exc import BusinessException
from starters.auth.service import provide_super_users_service, SuperUserService
from starters.auth.model.dto import AdminUserLogin
from starters.auth.model.ec import AuthEC


@post(
    path="/login",
    tags=["登陆"],
    dependencies={"super_users_service": Provide(provide_super_users_service)},
)
async def login(
    super_users_service: SuperUserService,
    data: Annotated[AdminUserLogin, Body(media_type=RequestEncodingType.URL_ENCODED)],
) -> None:
    obj = await super_users_service.get_one_or_none(
        super_users_service.model_type.userame == data.username
    )
    if obj is None or obj.password != data.password:
        raise BusinessException(AuthEC.LOGIN_FAILED)
    return jwt_auth.login(identifier=str(data.id), response_body=obj)
