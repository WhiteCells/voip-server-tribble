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

    @delete("/dialplans/{id:str}", status_code=HTTP_200_OK)
    async def deleteDialplan(self, id: str, dialplan_service: DialplanService) -> Response:
        success = dialplan_service.deleteDialplan(id)
        if not success:
            return jsonify(404, None, "Dialplan not found")
        return jsonify(200, None, "Success delete dialplan")

    @put("/dialplans/{id:str}")
    async def putDialplan(self, id: str, dto: PutDialplanDto, dialplan_service: DialplanService) -> Response:
        success = dialplan_service.putDialplan(dto)
        if not success:
            return jsonify(404, None, "Put Failed")
        return jsonify(200, None, "")

    @get("/dialplans/{id:str}")
    async def getDialplanById(self, id: str, dialplan_service: DialplanService) -> Response:
        success = dialplan_service.getDialplanById(id)
        return jsonify(200, None, "")
    
    @get("/dialplans")
    async def getDialplan(self, dialplan_service: DialplanService) -> Response:
        return jsonify(200, None, "")

    @post("/batch_dialplans")
    async def batchDialplan(self):
        return jsonify(200, None, "")