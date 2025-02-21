from litestar import Litestar
from starters import FullstackStarterPlugin


def create_app() -> Litestar:
    _app = Litestar(
        debug=True,
        plugins=[FullstackStarterPlugin()]
    )
    return _app


app = create_app()
