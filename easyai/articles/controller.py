from litestar import Controller, post, get
from litestar.di import Provide
from litestar.pagination import OffsetPagination
from litestar.repository.filters import LimitOffset

from easyai.articles.model.dto import ArticleInDTO, ArticleOutDTO
from easyai.articles.model.entity import Article
from easyai.articles.service import provide_article_service, ArticleService


class ArticleController(Controller):
    dto = ArticleInDTO
    return_dto = ArticleOutDTO
    path = "/articles"
    tags = ["文章"]

    dependencies = {"articles_service": Provide(provide_article_service)}

    @post("/")
    async def create_article(
        self, articles_service: ArticleService, data: Article
    ) -> Article:
        return await articles_service.create(data)

    @get("/")
    async def page_articles(
        self, articles_service: ArticleService, limit_offset: LimitOffset
    ) -> OffsetPagination[Article]:
        items, total = await articles_service.list_and_count(limit_offset)
        return OffsetPagination[Article](
            items=items,
            total=total,
            limit=limit_offset.limit,
            offset=limit_offset.offset,
        )
