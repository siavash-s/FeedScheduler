from config import get_conf
from redis import Redis
import publisher


# redis client
_redis = None


def get_redis():
    global _redis
    if _redis:
        return _redis
    else:
        _redis = Redis.from_url(get_conf().redis_url)
        return _redis


_publisher = None


def get_publisher():
    global _publisher
    if _publisher is None:
        _publisher = publisher.RabbitmqPublisher(
            get_conf().rabbitmq_url, get_conf().task_exchange,
            get_conf().routing_key, get_conf().rabbitmq_connection_retry,
            get_conf().rabbitmq_retry_interval
        )
    else:
        return _publisher
