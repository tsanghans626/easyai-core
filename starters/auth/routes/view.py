from litestar import get

from litestar.plugins.htmx import HTMXTemplate
from litestar.response import Template


@get("/admin/login")
def get_admin_login_view() -> Template:
    return HTMXTemplate(template_name="login.html.jinja")
