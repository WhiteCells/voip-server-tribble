"""

"""

from litestar import Controller, get, post, Response
from litestar.status_codes import HTTP_200_OK
from app.services.acc_service import AccService
from app.dto.acc_dto import CreateAccDto, PutAccDto
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

