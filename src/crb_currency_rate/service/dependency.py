from typing import TypeVar, Callable

from fast_depends import dependency_provider

from src.crb_currency_rate.common.marker.redis import RedisMarker
from src.crb_currency_rate.core import setup_redis
from src.crb_currency_rate.core.setting import Config
from src.crb_currency_rate.service.redis import RedisManager


DependencyType = TypeVar("DependencyType")


def singleton(value: DependencyType) -> Callable[[], DependencyType]:
    def singleton_factory() -> DependencyType:
        return value

    return singleton_factory


def init_dependency(config: Config) -> None:
    redis = setup_redis(config.redis)
    manager = RedisManager(redis)
    dependency_provider.override(RedisMarker, singleton(manager))
