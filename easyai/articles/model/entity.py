import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column
from advanced_alchemy.base import BigIntAuditBase


class Article(BigIntAuditBase):
    __tablename__ = "article"

    author: Mapped[str] = mapped_column(sa.String(1023), comment="作者")
    email: Mapped[str] = mapped_column(sa.String(1023), comment="电子邮箱")
    title: Mapped[str] = mapped_column(sa.String(1023), comment="标题")
    content: Mapped[str] = mapped_column(sa.Text, comment="内容")
