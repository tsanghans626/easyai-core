from litestar.plugins.sqlalchemy import SQLAlchemyDTO
from litestar.dto.config import DTOConfig
from easyai.articles.model.entity import Article


class ArticleInDTO(SQLAlchemyDTO[Article]):
    config = DTOConfig(exclude={"id", "created_at", "updated_at"})


ArticleOutDTO = SQLAlchemyDTO[Article]
