"""

"""

from litestar import Router
from app.controllers import AccController, ClientController, DialplanController

routes = [
    Router(path="/api", route_handlers=[
        AccController,
        ClientController,
        DialplanController,
    ])
]