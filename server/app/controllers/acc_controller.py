"""

"""

from litestar import Controller, get, post, put, delete, Response
from litestar.status_codes import HTTP_200_OK
from app.services.acc_service import AccService
from app.dto.acc_dto import CreateAccDto, PutAccDto, GetAccQuery
from app.utils.jsonify import jsonify
from app.utils.logger import logger


class AccController(Controller):

    @post(path="/accounts")
    async def createAcc(self, data: CreateAccDto, acc_service: AccService) -> Response:
        success, msg = await acc_service.createAcc(data)
        if not success:
            return jsonify(500, None, msg)
        return jsonify(200, None, msg)

    @delete(path="/accounts/{id:str}", status_code=HTTP_200_OK)
    async def deleteAcc(self, id: str, acc_service: AccService) -> Response:
        success = await acc_service.deleteAcc(id)
        if not success:
            return jsonify(404, None, "Account not found")
        return jsonify(200, None, "Succes delete")

    @put(path="/accounts/{id:str}")
    async def putAcc(self, id: str, dto: PutAccDto, acc_service: AccService) -> Response:
        success, msg = await acc_service.putAcc(id, dto)
        if not success:
            return jsonify(500, None, msg)
        return jsonify(200, None, msg)

    @get(path="/accounts/{id:str}")
    async def getAccById(self, id: str, acc_service: AccService) -> Response:
        acc = await acc_service.getAccById(id)
        return jsonify(200, acc, "")

    @get(path="/accounts")
    async def getAcc(self, query: GetAccQuery, acc_service: AccService) -> Response:
        if query.page < 1 or query.page_size > 20:
            return jsonify(405, None, "query foramt error")
        logger.info(f"get /accounts {query}")
        accs = await acc_service.getAccs(query)
        return jsonify(200, accs, "msg")
