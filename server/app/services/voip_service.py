"""

"""

from typing import AsyncGenerator
from app.repositories import VoipRepository
from app.dto import NotifyDto, HeartbeatDto
from app.utils.logger import logger

class VoipService:
    def __init__(self, voip_repository: VoipRepository):
        self.__voip_repository = voip_repository

    async def notify(self, dto: NotifyDto) -> dict:
        clientId = await self.__voip_repository.notify(dto)
        return {
            "clientId": clientId
        }

    async def heartbeat(self, clientId: str, dto: HeartbeatDto) -> str:
        await self.__voip_repository.heartbeat(clientId, dto)
        return ""
    
    async def getAccounts(self, clientId: str) -> str:
        await self.__voip_repository.get


async def provide_voip_service(voip_repository: VoipRepository) -> AsyncGenerator[VoipService, None]:
    yield VoipService(voip_repository)
