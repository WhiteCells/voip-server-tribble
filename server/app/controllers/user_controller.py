"""

"""

from litestar import Controller, get, post, put, delete, Response, Router
from litestar.status_codes import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from app.services.user_service import UserService
from app.dto.user_dto import CreateUserDTO, PutUserDTO
from app.utils.jsonify import jsonify
from app.utils.logger import logger


class UserController(Controller):

    @post(path="/users")
    async def create_user(self, data: CreateUserDTO, user_service: UserService) -> Response:
        logger.info("post /users")
        success, msg = await user_service.create_user(data)
        if not success:
            return jsonify(500, None, msg)
        return jsonify(200, None, msg)

    @get(path="/users/{user_id:int}")
    async def get_user_by_id(self, user_id: int, user_service: UserService) -> Response:
        logger.info("get /users/{user_id}")
        user =  await user_service.get_user_by_id(user_id)
        if not user:
            return jsonify(500, None, "error")
        return jsonify(200, user, "success")

    @get(path="/users")
    async def get_all_user(self, user_service: UserService) -> Response:
        logger.info("get /users")
        users = await user_service.get_all_user()
        if not users:
            return jsonify(500, None, "error")
        return jsonify(200, users, "success")

    @delete(path="/users/{user_id:int}", status_code=HTTP_200_OK) # HTTP_200_OK
    async def delete_user_by_id(self, user_id: int, user_service: UserService) -> Response:
        logger.info("delete /users/{user_id}")
        success, msg = await user_service.delete_user_by_id(user_id)
        if not success:
            return jsonify(500, None, msg)
        return jsonify(200, None, "success")

    @put(path="/users/{user_id:int}")
    async def put_user_by_id(self, user_id: int, dto: PutUserDTO, user_service: UserService) -> Response:
        logger.info("put /users/{user_id}")
        return jsonify(200, None, "success")