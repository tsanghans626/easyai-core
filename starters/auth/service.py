import sqlalchemy as sa

from typing import AsyncGenerator

from advanced_alchemy.repository import SQLAlchemyAsyncRepository
from advanced_alchemy.service import SQLAlchemyAsyncRepositoryService

from starters.config import settings
from starters.auth.model.entity import User, SuperUser

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine


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


async def init_superuser():
    engine = create_async_engine(settings.db.sqlalchemy_url)

    async with engine.connect() as conn:
        stmt = sa.select(User).where(User.is_superuser == True)
        result = await conn.execute(stmt)
        obj = result.scalar_one_or_none()

        if obj is None:
            async with conn.begin():
                stmt = sa.insert(User).values({"is_superuser": 1})
                result = await conn.execute(stmt)
                user_id = result.inserted_primary_key[0]

                stmt = sa.insert(SuperUser).values(
                    {
                        "user_id": user_id,
                        "username": settings.auth.superuser,
                        "password": settings.auth.superuser_pwd,
                    }
                )
                await conn.execute(stmt)
