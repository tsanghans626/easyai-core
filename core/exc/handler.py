import traceback

from litestar import Request, Response, MediaType
from litestar import status_codes
from core.config import settings
from core.exc import BusinessException, ServerException


def business_exception_handler(_: Request, exc: BusinessException):
    return Response(
        media_type=MediaType.JSON,
        content={"detail": {"code": exc.code, "msg": exc.msg}},
        status_code=status_codes.HTTP_400_BAD_REQUEST,
    )


def server_exception_handler(_: Request, exc: ServerException):
    detail = {"code": 999998, "msg": "请联系管理员"}
    if settings.env == "development":
        detail.update({"traceback": traceback.format_exc()})
        detail.update({"msg": exc.msg})

    return Response(
        media_type=MediaType.JSON,
        status_code=status_codes.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": detail},
    )


def unexpected_error_handler(_: Request, exc: Exception):
    detail = {"code": 999999, "msg": "请联系管理员"}
    if settings.env == "development":
        detail.update({"traceback": traceback.format_exc()})

    return Response(
        media_type=MediaType.JSON,
        status_code=status_codes.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": detail},
    )
