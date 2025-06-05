"""

"""

from typing import AsyncGenerator
from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession
from redis.asyncio import Redis
from app.dto.dialplan_dto import CreateDialplanDto, PutDialplanDto, GetFreeDialplanDto
from app.models.dialplan_model import Dialplan, DialplanStatus
from app.utils.logger import logger


class DialplanRepository:
    def __init__(self, db_session: AsyncSession, redisclient: Redis):
        self.__db_session = db_session
        self.__redisclient = redisclient

    async def createDialplan(self, dto: CreateDialplanDto) -> bool:
        try:
            new_dialplan = Dialplan(**dto.model_dump())
            self.__db_session.add(new_dialplan)
            await self.__db_session.commit()
            await self.__db_session.refresh(new_dialplan)
            return True
        except Exception as e:
            await self.__db_session.rollback()
            logger.error(f"Failed to create Dialplan {e}")
            return False

    async def putDialplan(self, dto: PutDialplanDto) -> bool:
        try:
            # 查找现有记录
            result = await self.__db_session.execute(
                select(Dialplan).where(Dialplan.id == dto.phone)
            )
            dialplan = result.scalar_one_or_none()

            if dialplan is None:
                logger.warning(f"Dialplan with phone={dto.phone} not found.")
                return False

            # 更新字段（跳过 id）
            update_data = dto.model_dump(exclude={"id"})
            for key, value in update_data.items():
                setattr(dialplan, key, value)

            await self.__db_session.commit()
            await self.__db_session.refresh(dialplan)
            return True

        except Exception as e:
            await self.__db_session.rollback()
            logger.error(f"Failed to update Dialplan {dto}: {e}")
            return False
        
    # todo
    async def getFreeDialplan(self, cnt: int) -> GetFreeDialplanDto:
        try:
            stmt = select(Dialplan).where(Dialplan.status == DialplanStatus.Free).limit(cnt)
        except Exception as e:
            return []

    async def exist_dialplan(self, phone: str) -> bool:
        stmt = select(Dialplan).where(Dialplan.phone == phone)
        result = await self.__db_session.execute(stmt)
        return result.scalar_one_or_none() is not None       

async def provide_dialplan_repository(db_session: AsyncSession,
                                      redisclient: Redis) -> AsyncGenerator[DialplanRepository, None]:
    yield DialplanRepository(db_session, redisclient)
