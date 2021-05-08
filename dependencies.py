from config import get_conf
from redis import Redis
import publisher
import loop
import data


# redis client
_redis = None


def get_redis():
    global _redis
    if _redis:
        return _redis
    else:
        _redis = Redis.from_url(get_conf().redis_url)
        return _redis


_channel_set = data.ActiveChannelSet()


_publisher = publisher.RabbitmqPublisher(
    get_conf().rabbitmq_url, get_conf().task_exchange,
    get_conf().routing_key, get_conf().rabbitmq_connection_retry,
    get_conf().rabbitmq_retry_interval
)


main_loop = loop.MainLoop(_publisher, _channel_set, get_conf().publish_interval)
