"""

"""

from typing import AsyncGenerator
from app.dto.acc_dto import CreateAccDto, PutAccDto
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


async def provide_acc_service(acc_repository: AccRepository) -> AsyncGenerator[AccService, None]:
    yield AccService(acc_repository)
