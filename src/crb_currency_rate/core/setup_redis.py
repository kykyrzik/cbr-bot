from redis.asyncio import Redis

from src.crb_currency_rate.core.setting import RedisConfig


def setup_redis(config: RedisConfig) -> Redis:
    return Redis(host=config.redis_host,
                 port=config.redis_port)  # type: ignore
