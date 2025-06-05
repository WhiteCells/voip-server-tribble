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
    async def createClient(self, data: CreateClientDto, client_service: ClientService) -> Response:
        logger.info("post /clients")
        success, msg = await client_service.createClient(data)
        if not success:
            return jsonify(500, None, msg)
        return jsonify(200, None, msg)
    
    @delete(path="/clients/${clientId}", status_code=HTTP_200_OK)
    async def deleteClient(self, clientId: str, client_service: ClientService) -> Response:
        await client_service.deleteClient(clientId)
        return jsonify(200, None, "")

    @get(path="/clients")
    async def getClient(self, client_service: ClientService) -> Response:
        return jsonify(200, None, "")