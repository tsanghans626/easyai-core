from litestar.plugins.htmx import HTMXRequest, HTMXTemplate
from litestar import get
from litestar.response import Template


@get(path="/htmx/hello")
def get_form(request: HTMXRequest) -> Template:
    if request.htmx:  # if request has "HX-Request" header, then
        print(request.htmx)  # HTMXDetails instance
        print(request.htmx.current_url)
    return HTMXTemplate(template_name="hello.html")
