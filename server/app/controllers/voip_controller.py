"""

"""

from litestar import Controller, get, post, put, delete, Response
from litestar.status_codes import HTTP_200_OK
from app.services import VoipService
from app.utils.jsonify import jsonify
from app.utils.logger import logger
from app.dto import NotifyDto, HeartbeatDto


class VoipController(Controller):

    @post(path="/notify")
    async def notify(self, data: NotifyDto, voip_service: VoipService) -> Response:
        """
        返回已有的且空闲的客户端 UUID
        """
        logger.info(f"post /notify {data}")
        d = await voip_service.notify(data)
        return jsonify(200, d, "")

    @post(path="/heartbeat/{clientId:str}")
    async def heartbeat(self, clientId: str, data: HeartbeatDto, voip_service: VoipService) -> Response:
        """
        接受客户端发送的心跳
        通过 redis 有效期的 key 实现
        """
        logger.info(f"post /heartbeat/{clientId}")
        await voip_service.heartbeat(clientId, data)
        return jsonify(200, "None", "")

    @get(path="/accounts/{clientId:str}")
    async def getAccounts(self, clientId: str, voip_service: VoipService) -> Response:
        """
        每个客户端的账号上限暂时是 3 个
        如果修改了客户端的账号分配应该如何处理
        """
        logger.info(f"get /accounts/{clientId}")
        await voip_service.getAccounts(clientId)
        return jsonify(200, None, "")

    @post(path="/reg_status/{clientId:str}")
    async def postRegStatus(self, clientId: str) -> Response:
        """
        账号注册状态
        """
        logger.info(f"post /reg_status/{clientId}")
        return jsonify(200, None,  "")

    @get(path="/dialplans/{clientId:str}")
    async def getDialplans(self, clientId: str) -> Response:
        """
        获取空闲的呼叫号码
        """
        logger.info(f"get /dialplans/{clientId}")
        return jsonify(200, None, "")

    @post(path="/dial_status/{clientId:str}")
    async def postDialStatus(self, clientId: str) -> Response:
        """
        接收拨打状态
        """
        logger.info(f"post /dial_status/{clientId}")
        return jsonify(200, None, "")

    @post(path="/dial_wav/{clientId:str}")
    async def postDialWav(self, clientId: str) -> Response:
        """
        接受拨打音频
        """
        logger.info(f"post /dial_wav/{clientId}")
        return jsonify(200, None, "")
