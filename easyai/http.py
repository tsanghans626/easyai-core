from litestar import Litestar
from htmx_fullstack_starter import FullstackStarterPlugin

def create_app() -> Litestar:
    _app = Litestar(debug=True, plugins=[FullstackStarterPlugin()])
    return _app


app = create_app()
