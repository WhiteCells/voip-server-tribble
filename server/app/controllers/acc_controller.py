"""

"""

from litestar import Controller, get, post, delete, Response
from litestar.status_codes import HTTP_200_OK
from app.services.acc_service import AccService
from app.dto.acc_dto import CreateAccDto, PutAccDto, GetAccQuery
from app.utils.jsonify import jsonify
from app.utils.logger import logger


class AccController(Controller):

    @post(path="/accounts")
    async def createAccount(self, data: CreateAccDto, acc_service: AccService) -> Response:
        logger.info("post /accounts")
        success, msg = await acc_service.createAcc(data)
        if not success:
            return jsonify(500, None, msg)
        return jsonify(200, None, msg)
    
    @delete(path="/accounts")
    async def deleteAccount(self, )

    @get(path="/accounts")
    async def getAccount(self, query: GetAccQuery, acc_service: AccService) -> Response:
        logger.info(f"get /accounts {query}")
        accs = await acc_service.getAcc(query)
        return jsonify(200, accs, "msg")
