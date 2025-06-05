"""

"""


import json
from sqlalchemy.ext.asyncio import AsyncSession
from redis.asyncio import Redis
from sqlalchemy import select, delete
from app.dto.user_dto import GetUserDTO, CreateUserDTO
from app.models.user_model import User
from app.utils.logger import logger

class UserRepository:
    def __init__(self, db_session: AsyncSession, redisclient: Redis):
        self.__db_session = db_session
        self.__redisclient = redisclient

    async def create_user(self, dto: CreateUserDTO) -> bool:
        try:
            new_user = User(**dto.model_dump())
            self.__db_session.add(new_user)
            await self.__db_session.commit()
            await self.__db_session.refresh(new_user)
            user_dto = GetUserDTO(id=new_user.id, username=new_user.username, email=new_user.email)
            cache_key = f"user:{new_user.id}"
            await self.__redisclient.set(cache_key, user_dto.model_dump_json(), ex=3600)
            return True

        except Exception as e:
            await self.__db_session.rollback()
            logger.error(f"failed to create user {dto}")
            return False

    async def get_user_by_id(self, user_id: int) -> GetUserDTO:
        # cache_key = f"user:{user_id}"
        # cached_user = await self.__redisclient.get(cache_key)
        # if cached_user:
        #     user_data = json.loads(cached_user)
        #     return GetUserDTO(**user_data)

        stmt = select(User).where(User.id == user_id)
        result = await self.__db_session.execute(stmt)
        user = result.scalar_one_or_none()
        if not user:
            return None

        user_dto = GetUserDTO(id=user.id, username=user.username, email=user.email)

        # 缓存
        # await self.__redisclient.set(cache_key, user_dto.model_dump_json(), ex=3600)

        return user_dto

    async def get_all_user(self) -> list[GetUserDTO]:
        # cache_key = "users:all"
        # cached_users = await self.__redisclient.get(cache_key)
        # if cached_users:
        #     user_list = json.loads(cached_users)
        #     return [GetUserDTO(**user) for user in user_list]

        stmt = select(User)
        result = await self.__db_session.execute(stmt)
        users = result.scalars().all()

        dto_list = [GetUserDTO(id=u.id, username=u.username, email=u.email) for u in users]

        # 缓存序列化成json字符串
        # await self.__redisclient.set(cache_key, json.dumps([dto.model_dump() for dto in dto_list]), ex=3600)

        return dto_list
    
    async def delete_user_by_id(self, user_id) -> bool:
        try:
            stmt = delete(User).where(User.id == user_id)
            await self.__db_session.execute(stmt)
            await self.__db_session.commit()
            return True
        except Exception as e:
            await self.__db_session.rollback()
            logger.error(f"Failed to delete user {user_id}: {e}")
            return False
    
    async def exist_email(self, email: str) -> bool:
        stmt = select(User).where(User.email == email)
        result = await self.__db_session.execute(stmt)
        return result.scalar_one_or_none() is not None
