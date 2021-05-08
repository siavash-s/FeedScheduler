from pydantic import (
    BaseSettings,
    Field, RedisDsn
)
from enum import Enum


class Config(BaseSettings):
    class _LogLevel(str, Enum):
        info = "INFO"
        debug = "DEBUG"
        warning = "WARNING"
    log_level: _LogLevel = Field('INFO', env='LOG_LEVEL')

    redis_url: RedisDsn = Field(..., env="REDIS_URL")

    redis_channels_set: str = Field("channels", env="REDIS_CHANNELS_SET")


settings = None


def get_conf():
    global settings
    if settings is not None:
        return settings
    else:
        settings = Config()
        return settings
