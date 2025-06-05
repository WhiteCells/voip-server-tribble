"""

"""

from app.dto.user_dto import CreateUserDTO, GetUserDTO
from app.repositories.user_repository import UserRepository

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.__user_repository = user_repository

    async def create_user(self, dto: CreateUserDTO) -> tuple[bool, str]:
        if await self.__user_repository.exist_email(dto.email):
            return False, "email exist"
        success = await self.__user_repository.create_user(dto)
        if not success:
            return False, "Failed create success"
        return True, "Create success"

    async def get_user_by_id(self, user_id: int) -> GetUserDTO:
        user = await self.__user_repository.get_user_by_id(user_id)
        return GetUserDTO.model_validate(user.model_dump()) if user else None

    async def get_all_user(self) -> list[GetUserDTO]:
        users = await self.__user_repository.get_all_user()
        return [GetUserDTO.model_validate(user.model_dump()) for user in users]

    async def delete_user_by_id(self, user_id: int) -> tuple[bool, str]:
        user = await self.__user_repository.get_user_by_id(user_id)
        if not user:
            return False, "user not exist"
        success = await self.__user_repository.delete_user_by_id(user_id)
        if not success:
            return False, "Failed delete"
        return True, "success"
