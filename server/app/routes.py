"""

"""

from litestar import Router
from app.controllers import (
    AccController, 
    ClientController, 
    DialplanController, 
    VoipController
)

routes = [
    Router(path="/api", route_handlers=[
        AccController,
        ClientController,
        DialplanController,
    ]),
    Router(path="/voip", route_handlers=[
        VoipController,
    ])
]