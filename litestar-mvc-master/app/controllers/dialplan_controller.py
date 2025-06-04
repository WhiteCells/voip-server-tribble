"""

"""

from litestar import Controller, get, post, put, delete, Response
from litestar.status_codes import HTTP_200_OK
from app.services import DialplanService
from app.dto import CreateDialplanDto, PutDialplanDto
from app.utils.jsonify import jsonify


class DialplanController(Controller):
    
    @post("/dialplans")
    async def createDialplan(self, data: CreateDialplanDto, dialplan_service: DialplanService) -> Response:
        success, msg = await dialplan_service.createDialplan(data)
        if not success:
            return jsonify(500, None, msg)
        return jsonify(200, None, msg)

