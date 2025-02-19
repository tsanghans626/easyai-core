from litestar.plugins.sqlalchemy import SQLAlchemyAsyncConfig
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from core.config import settings
from core.utils import get_s_timestamp


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True, comment="自增ID")
    created_at: Mapped[int] = mapped_column(default=get_s_timestamp, comment="创建时间")
    updated_at: Mapped[int] = mapped_column(
        default=get_s_timestamp, onupdate=get_s_timestamp, comment="更新时间"
    )


db_config = SQLAlchemyAsyncConfig(
    connection_string=settings.db.sqlalchemy_url,
    metadata=Base.metadata,
    create_all=True,
)