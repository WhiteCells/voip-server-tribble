"""

"""

from typing import AsyncGenerator
from app.dto.dialplan_dto import CreateDialplanDto, PutDialplanDto
from app.repositories.dialplan_repository import DialplanRepository


class DialplanService:
    def __init__(self, dialplan_repository: DialplanRepository):
        self.__dialplan_repository = dialplan_repository

    async def createDialplan(self, dto: CreateDialplanDto) -> tuple[bool, str]:
        if await self.__dialplan_repository.exist_dialplan(dto.phone):
            return False, "dialplan exist"
        success = await self.__dialplan_repository.createDialplan(dto)
        if not success:
            return False, "Failed create"
        return True, "Create Success"

    async def putDialplan(self, dto: PutDialplanDto) -> tuple[bool, str]:
        await self.__dialplan_repository.putDialplan(dto)
        return True, "Put Success"
    

async def provide_dialplan_service(dialplan_repository: DialplanRepository) -> AsyncGenerator[DialplanService, None]:
    yield DialplanService(dialplan_repository)
