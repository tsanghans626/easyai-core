import msgspec

from litestar.plugins.sqlalchemy import SQLAlchemyDTO
from litestar.dto.config import DTOConfig

from easyai.users.model.entity import AdminUser


class AdminUserLogin(msgspec.Struct):
    username: str
    password: str


class AdminUserOutDTO(SQLAlchemyDTO[AdminUser]):
    config = DTOConfig(include={"user_id", "username"})
