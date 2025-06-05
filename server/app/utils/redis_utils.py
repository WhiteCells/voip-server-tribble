import redis
from typing import Optional, Any
from utils.redisclient.redisclient import redis_client

class RedisUtils:

    def set(self, key: str, value: Any, expire: Optional[int] = None) -> None:
        """
        设置键值对
        :param key: 键
        :param value: 值
        :param expire: 过期时间（秒）
        """
        redis_client.set(key, value)
        if expire:
            redis_client.expire(key, expire)

    def get(self, key: str) -> Optional[bytes]:
        """
        获取键对应的值
        :param key: 键
        :return: 值，如果不存在则返回 None
        """
        return redis_client.get(key)

    def delete(self, key: str) -> int:
        """
        删除键值对
        :param key: 键
        :return: 删除的键的数量
        """
        return redis_client.delete(key)

    def exists(self, key: str) -> bool:
        """
        检查键是否存在
        :param key: 键
        :return: 如果存在返回 True，否则返回 False
        """
        return redis_client.exists(key)
