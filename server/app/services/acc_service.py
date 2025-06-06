"""

"""

from typing import AsyncGenerator
from app.dto.acc_dto import CreateAccDto, PutAccDto, GetAccDto, GetAccQuery
from app.repositories.acc_repository import AccRepository


class AccService:
    def __init__(self, acc_repository: AccRepository):
        self.__acc_repository = acc_repository

    async def createAcc(self, dto: CreateAccDto) -> bool:
        success = await self.__acc_repository.createAcc(dto)
        if not success:
            return False, "Failed create"
        return True, "Create Success"
    
    async def deleteAcc(self, id: str) -> bool:
        return await self.__acc_repository.deleteAcc(id)

    async def putAcc(self, id: str, dto: PutAccDto) -> bool:
        success = await self.__acc_repository.putAcc(dto)
        if not success:
            return False, "Failed Put"
        return True, "Put Success"
    
    async def getAccById(self, id: str) -> GetAccDto:
        acc = await self.__acc_repository.getAccById(id)
        return GetAccDto.model_validate(acc.model_dump())

    async def getAccs(self, query: GetAccQuery) -> list[GetAccDto]:
        accs = await self.__acc_repository.getAccs(query)
        return [GetAccDto.model_validate(acc.model_dump()) for acc in accs]


async def provide_acc_service(acc_repository: AccRepository) -> AsyncGenerator[AccService, None]:
    yield AccService(acc_repository)
