"""

"""

from typing import AsyncGenerator
from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession
from redis.asyncio import Redis
from app.dto.client_dto import CreateClientDto, PutClientDto, GetClientDto, GetClientsQuery
from app.models.client_model import Client
from app.utils.logger import logger


class ClientRepository:
    def __init__(self, db_session: AsyncSession, redisclient: Redis):
        self.__db_session = db_session
        self.__redisclient = redisclient

    async def createClient(self, dto: CreateClientDto) -> bool:
        try:
            new_client = Client(**dto.model_dump())
            self.__db_session.add(new_client)
            await self.__db_session.commit()
            await self.__db_session.refresh(new_client)
            return True
        except Exception as e:
            await self.__db_session.rollback()
            logger.error(f"Failed to create Client {e}")
            return False
        
    async def deleteClient(self, id: int) -> bool:
        try:
            result = await select(Client).where(Client.id == id)
        except Exception as e:
            return False

    async def putClient(self, dto: PutClientDto) -> bool:
        try:
            result = await self.__db_session.execute(
                select(Client).where(Client.name == dto.name)
            )
            client = result.scalar_one_or_none()

            if client is None:
                logger.warning(f"Dialplan with name={dto.name}")
                return False

            update_data = dto.model_dump(exclude={"id"})
            for key, value in update_data.items():
                setattr(client, key, value)

            await self.__db_session.commit()
            await self.__db_session.refresh(client)
            return True

        except Exception as e:
            await self.__db_session.rollback()
            logger.error(f"Failed to update client {e.__str__}")
            return False
        
    async def getClientById(self, id: str) -> GetClientDto:
        stmt = select(Client).where(Client.id == id)
        result = await self.__db_session.execute(stmt)
        return result.scalar_one_or_none()

    async def getClients(self, query: GetClientsQuery) -> list[GetClientDto]:
        offset = (query.page - 1) * query.page_size
        stmt = select(Client).offset(offset).limit(query.page_size)
        result = await self.__db_session.execute(stmt)
        clients = result.all()
        dto_list = [GetClientDto(c) for c in clients]
        return dto_list

    async def existClient(self, id: str) -> bool:
        stmt = select(Client).where(Client.id == id)
        result = await self.__db_session.execute(stmt)
        return result.scalar_one_or_none() is not None


async def provide_client_repository(db_session: AsyncSession, 
                                    redisclient: Redis) -> AsyncGenerator[ClientRepository, None]:
    return ClientRepository(db_session, redisclient)
