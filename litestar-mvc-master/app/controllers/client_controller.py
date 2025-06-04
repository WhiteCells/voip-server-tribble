"""

"""

from litestar import Controller, get, post, put, delete, Response
from litestar.status_codes import HTTP_200_OK
from app.services import ClientService
from app.dto import CreateClientDto, PutClientDto
from app.utils.jsonify import jsonify
from app.utils.logger import logger


class ClientController(Controller):

    @post(path="/clients")
    async def create_client(self, data: CreateClientDto, client_service: ClientService) -> Response:
        logger.info("post /clients")
        success, msg = await client_service.createClient(data)
        if not success:
            return jsonify(500, None, msg)
        return jsonify(200, None, msg)
