import traceback

from litestar import Request, Response, MediaType
from litestar import status_codes
from litestar.exceptions import NotFoundException
from litestar.plugins.htmx import HTMXTemplate
from litestar.response import Template
from starters.config import settings
from starters.exc import BusinessException


def business_exception_handler(_: Request, exc: BusinessException):
    return HTMXTemplate(
        template_name="error.html.jinja",
        context={"error_msg": exc.msg},
        re_swap="outerHTML",
        re_target="#error",
    )


def unexpected_error_handler(_: Request, exc: Exception):
    return HTMXTemplate(
        template_name="error.html.jinja",
        context={"error_msg": "请联系管理员"},
        re_swap="outerHTML",
        re_target="#error",
    )


def notfound_handler(_: Request, exc: NotFoundException) -> Template:
    return HTMXTemplate(template_name="404.html.jinja")
