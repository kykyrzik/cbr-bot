from decimal import Decimal
from typing import Final, Self

from redis.asyncio import Redis


ONE_DAY: Final[int] = 86_400


class RedisManager:
    __slots__ = ("_redis",)

    def __init__(self, redis: Redis) -> None:
        self._redis = redis

    async def set(self, code: str, value: Decimal) -> None:
        await self._redis.set(code, str(value), ex=ONE_DAY)
