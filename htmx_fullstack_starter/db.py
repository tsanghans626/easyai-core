from litestar.params import Parameter
from litestar.plugins.sqlalchemy import filters
from litestar.plugins.sqlalchemy import (
    SQLAlchemyAsyncConfig,
    AsyncSessionConfig,
    SQLAlchemyPlugin,
)
from advanced_alchemy.base import BigIntAuditBase
from htmx_fullstack_starter.config import settings


session_config = AsyncSessionConfig(expire_on_commit=False)
sqlalchemy_config = SQLAlchemyAsyncConfig(
    connection_string=settings.db.sqlalchemy_url,
    metadata=BigIntAuditBase.metadata,
    before_send_handler="autocommit",
    session_config=session_config,
    create_all=True,
)
alchemy = SQLAlchemyPlugin(config=sqlalchemy_config)


def provide_limit_offset_pagination(
    current_page: int = Parameter(ge=1, query="currentPage", default=1, required=False),
    page_size: int = Parameter(
        query="pageSize",
        ge=1,
        default=10,
        required=False,
    ),
) -> filters.FilterTypes:
    return filters.LimitOffset(page_size, page_size * (current_page - 1))
