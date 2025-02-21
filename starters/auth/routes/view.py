from litestar.plugins.htmx import HTMXTemplate
from litestar import get
from litestar.response import Template


@get(path="/login")
def login_view() -> Template:
    return HTMXTemplate(template_name="login.html.jinja")
