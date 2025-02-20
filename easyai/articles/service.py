from typing import AsyncGenerator

from advanced_alchemy.repository import SQLAlchemyAsyncRepository
from advanced_alchemy.service import SQLAlchemyAsyncRepositoryService
from easyai.articles.model.entity import Article

from sqlalchemy.ext.asyncio import AsyncSession


class ArticleRepo(SQLAlchemyAsyncRepository[Article]):
    model_type = Article


async def provide_articles_repo(db_session: AsyncSession) -> ArticleRepo:
    return ArticleRepo(session=db_session)


class ArticleService(SQLAlchemyAsyncRepositoryService[Article]):
    repository_type = ArticleRepo


async def provide_article_service(
    db_session: AsyncSession,
) -> AsyncGenerator[ArticleService, None]:
    async with ArticleService.new(session=db_session) as service:
        yield service
