from pydantic import (
    BaseSettings,
    Field, RedisDsn, PositiveInt
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

    rabbitmq_url: str = Field(..., env="RABBITMQ_URL")

    rabbitmq_retry_interval: PositiveInt = Field(
        10, env="RABBITMQ_RETRY_INTERVAL", description="RabbitMQ connection retry interval"
    )

    rabbitmq_connection_retry: PositiveInt = Field(10, env="RABBITMQ_CONNECTION_RETRY")

    task_exchange: str = Field(
        'task_exchange', env="TASK_EXCHANGE",
        description="RabbitMQ exchange name to send tasks to"
    )

    routing_key: str = Field("task", env="ROUTING_KEY", description="RabbitMQ routing key for sending tasks")


settings = None


def get_conf():
    global settings
    if settings is not None:
        return settings
    else:
        settings = Config()
        return settings
