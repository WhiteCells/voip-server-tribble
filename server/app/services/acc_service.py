"""

"""

from typing import AsyncGenerator
from app.dto.acc_dto import CreateAccDto, PutAccDto, GetAccDto, GetAccQuery
from app.repositories.acc_repository import AccRepository


class AccService:
    def __init__(self, acc_repository: AccRepository):
        self.__acc_repository = acc_repository

    async def createAcc(self, dto: CreateAccDto) -> bool:
        # if await self.__acc_repository.existAcc(dto.name):
        #     return False, "acc exist"
        success = await self.__acc_repository.createAcc(dto)
        if not success:
            return False, "Failed create"
        return True, "Create Success"

    async def putAcc(self, dto: PutAccDto) -> bool:

        return True, "Put Success"

    async def getAcc(self, query: GetAccQuery) -> list[GetAccDto]:
        accs = await self.__acc_repository.getAcc(query)
        return [GetAccDto.model_validate(acc.model_dump()) for acc in accs]


async def provide_acc_service(acc_repository: AccRepository) -> AsyncGenerator[AccService, None]:
    yield AccService(acc_repository)
