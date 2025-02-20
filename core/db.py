from litestar.plugins.sqlalchemy import (
    SQLAlchemyAsyncConfig,
    AsyncSessionConfig,
    SQLAlchemyPlugin,
)
from advanced_alchemy.base import BigIntAuditBase
from core.config import settings


session_config = AsyncSessionConfig(expire_on_commit=False)
sqlalchemy_config = SQLAlchemyAsyncConfig(
    connection_string=settings.db.sqlalchemy_url,
    metadata=BigIntAuditBase.metadata,
    before_send_handler="autocommit",
    session_config=session_config,
    create_all=True,
)
alchemy = SQLAlchemyPlugin(config=sqlalchemy_config)
