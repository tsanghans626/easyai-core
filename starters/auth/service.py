from typing import AsyncGenerator

from advanced_alchemy.repository import SQLAlchemyAsyncRepository
from advanced_alchemy.service import SQLAlchemyAsyncRepositoryService

from starters.auth.model.entity import User, SuperUser

from sqlalchemy.ext.asyncio import AsyncSession


class UserRepo(SQLAlchemyAsyncRepository[User]):
    model_type = User


class UserService(SQLAlchemyAsyncRepositoryService[User]):
    repository_type = UserRepo


async def provide_user_service(
    db_session: AsyncSession,
) -> AsyncGenerator[UserService, None]:
    async with UserService.new(session=db_session) as service:
        yield service


class SuperUserRepo(SQLAlchemyAsyncRepository[SuperUser]):
    model_type = SuperUser


class SuperUserService(SQLAlchemyAsyncRepositoryService[SuperUser]):
    repository_type = SuperUserRepo


async def provide_super_users_service(
    db_session: AsyncSession,
) -> AsyncGenerator[SuperUserService, None]:
    async with SuperUserService.new(session=db_session) as service:
        yield service
