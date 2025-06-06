"""

"""

from typing import AsyncGenerator
from app.dto.client_dto import CreateClientDto, PutClientDto, GetClientDto, GetClientsQuery
from app.repositories.client_repository import ClientRepository


class ClientService:
    def __init__(self, client_repository: ClientRepository):
        self.__client_repository = client_repository

    async def createClient(self, dto: CreateClientDto) -> tuple[bool, str]:
        success = await self.__client_repository.createClient(dto)
        if not success:
            return False, "Failed create"
        return True, "Create Success"

    async def deleteClient(self, clientId: str) -> tuple[bool, str]:
        if await self.__client_repository.existClient(clientId):
            return False, "not exist"
        success = await self.__client_repository.deleteClient(clientId)
        if not success:
            return False, "Failed delete"
        return True, "Success delete"

    async def putClient(self, dto: PutClientDto) -> tuple[bool, str]:
        await self.__client_repository.putClient(dto)
        return True, "Put Success"

    async def getClientById(self, id: str) -> GetClientDto:
        return None

    async def getClients(self, query: GetClientsQuery) -> list[GetClientDto]:
        clients = await self.__client_repository.getClients()
        return clients


async def provide_client_service(client_repository: ClientRepository) -> AsyncGenerator[ClientService, None]:
    yield ClientService(client_repository)
