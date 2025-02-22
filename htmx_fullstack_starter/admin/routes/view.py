from litestar import get, Request

from litestar.plugins.htmx import HTMXTemplate
from litestar.response import Template

@get("/admin")
async def get_admin_view(request: Request) -> Template:
    print(request.user)
    return HTMXTemplate(
        template_name="admin.html.jinja",
    )