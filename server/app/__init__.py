"""

"""

from litestar import Litestar
from app.routes import routes
from app.dependencies import dependencies
from app.startup import startups
from app.config import Config

app = Litestar(
    route_handlers=routes,
    dependencies=dependencies,
    on_startup=[startups],
    debug=Config.DEBUG,
)