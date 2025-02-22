import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column
from advanced_alchemy.base import BigIntAuditBase


class User(BigIntAuditBase):
    role: Mapped[int] = mapped_column(default=0, comment="角色")
    is_superuser: Mapped[bool] = mapped_column(comment="是否超级管理员")


class SuperUser(BigIntAuditBase):
    __tablename__ = "super_user"

    user_id: Mapped[int] = mapped_column(comment="用户ID")
    username: Mapped[str] = mapped_column(sa.String(1023), comment="用户名")
    password: Mapped[str] = mapped_column(sa.String(1023), comment="密码")
