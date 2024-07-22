import configparser
from dataclasses import dataclass
from pathlib import Path


def get_path_to_setting() -> Path:
    return Path(__file__).parent.parent.parent.parent / 'dependencies.ini'


@dataclass
class RedisConfig:
    redis_host: str
    redis_port: int


@dataclass
class Config:
    redis: RedisConfig


def load_config() -> Config:
    config = configparser.ConfigParser()
    path = get_path_to_setting()
    config.read(path)

    return Config(
        redis=RedisConfig(**config["redis"])
    )