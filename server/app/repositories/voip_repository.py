"""

"""

from typing import AsyncGenerator
from sqlalchemy import select, delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from redis.asyncio import Redis
from app.dto import NotifyDto, HeartbeatDto, GetAccDto
from app.models import Client, ClientStatus, Acc, AccStatus
from datetime import datetime
from app.utils.logger import logger


class VoipRepository:

    def __init__(self, db_session: AsyncSession, redisclient: Redis):
        self.__db_session = db_session
        self.__redisclient = redisclient

    async def notify(self, dto: NotifyDto) -> str:
        """
        获取状态为空闲的客户端，返回其客户端 ID
        """
        stmt = select(Client).where(Client.status == ClientStatus.Offline)
        result = await self.__db_session.execute(stmt)
        client = result.scalars().first()
        if client:
            return client.id
        return None

    async def heartbeat(self, clientId: str, dto: HeartbeatDto) -> bool:
        """
        客户端心跳，更新客户端的更新时间，使用 redis 有效期 key
        """
        try:
            logger.info("heartbeat")
            # redis
            key = f"client:heartbeat:{clientId}"
            await self.__redisclient.set(key, "1", ex=5)
            # db
            stmt = update(Client).where(Client.id == clientId).values(
                update_at=datetime.now(),
                # status=ClientStatus.Online,
            )
            await self.__db_session.execute(stmt)
            await self.__db_session.commit()
            return True
        except Exception as e:
            await self.__db_session.rollback()
            return False
        
    async def getAccounts(self, clientId: str) -> list[GetAccDto]:
        """
        """
        try:
            # 找到对应的客户端，获取客户端的线程数
            stmt = select(Client).where(Client.id == clientId)
            result = await self.__db_session.execute(stmt)
            client = result.scalar_one_or_none()
            if not client:
                raise Exception("client not exists")
            # 根据客户端线程数获取对应的 Acc 数量
            stmt = select(Acc).where(Acc.client_id == clientId 
                                     and Acc.status == AccStatus.Offline).limit(client.thread_num)
            result = await self.__db_session.execute(stmt)
            accs = result.scalars().all()
            accs_dto = [
                GetAccDto(id=a.id, name=a.name, pwd=a.pwd, host=a.host) 
                for a in accs
            ]
            return accs_dto
        except Exception as e:
            logger.error(f"{e}")
            return None


async def provide_voip_repository(db_session: AsyncSession, 
                                  redisclient: Redis) -> AsyncGenerator[VoipRepository, None]:
    yield VoipRepository(db_session, redisclient)
