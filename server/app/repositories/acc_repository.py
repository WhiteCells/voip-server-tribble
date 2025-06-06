"""

"""

from typing import AsyncGenerator
from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession
from redis.asyncio import Redis
from app.dto.acc_dto import CreateAccDto, PutAccDto, GetAccDto, GetAccQuery
from app.models.acc_model import Acc
from app.utils.logger import logger


class AccRepository:
    def __init__(self, db_session: AsyncSession, redisclient: Redis):
        self.__db_session = db_session
        self.__redisclient = redisclient

    async def createAcc(self, dto: CreateAccDto) -> bool:
        try:
            new_acc = Acc(**dto.model_dump())
            self.__db_session.add(new_acc)
            await self.__db_session.commit()
            await self.__db_session.refresh(new_acc)
            return True
        except Exception as e:
            await self.__db_session.rollback()
            logger.error(f"Failed to create Acc {e}")
            return False
        
    async def deleteAcc(self, id: str) -> bool:
        try:
            stmt = delete(Acc).where(Acc.id == id)
            resutl = await self.__db_session.execute(stmt)
            await self.__db_session.commit()
            return resutl.rowcount > 0
        except Exception as e:
            await self.__db_session.rollback()
            logger.error(f"Failed to delete acc {e}")
            return False

    async def putAcc(self, dto: PutAccDto) -> bool:
        try:
            stmt = select(Acc).where(Acc.id == dto.name)
            result = await self.__db_session.execute(stmt)
            acc = result.scalar_one_or_none()

            if acc is None:
                logger.warning(f"Acc with name={dto.name} not found.")
                return False
            
            update_data = dto.model_dump(exclude={"id"})
            for key, value in update_data.items():
                setattr(acc, key, value)

            await self.__db_session.commit()
            await self.__db_session.refresh(acc)
            return True

        except Exception as e:
            await self.__db_session.rollback()
            logger.error(f"Failed to update acc {e}")
            return False

    async def getAccById(self, id: str) -> GetAccDto:
        stmt = select(Acc).where(Acc.id == id)
        result = await self.__db_session.execute(stmt)
        acc = result.scalar_one_or_none()
        if acc is None:
            return None
        dto = GetAccDto(id=acc.id, name=acc.name, pwd=acc.pwd, host=acc.host)
        return dto

    async def getAccs(self, query: GetAccQuery) -> list[GetAccDto]:
        offset = (query.page - 1) * query.page_size
        stmt = select(Acc).offset(offset).limit(query.page_size)
        result = await self.__db_session.execute(stmt)
        accs = result.scalars().all()
        dto_list = [GetAccDto(id=a.id, name=a.name, pwd=a.pwd, host=a.host) for a in accs]
        return dto_list

    async def existAcc(self, name: str) -> bool:
        stmt = select(Acc).where(Acc.name == name)
        result = await self.__db_session.execute(stmt)
        return result.scalar_one_or_none() is not None


async def provide_acc_repository(db_session: AsyncSession, 
                                 redisclient: Redis) -> AsyncGenerator[AccRepository, None]:
    yield AccRepository(db_session, redisclient)
