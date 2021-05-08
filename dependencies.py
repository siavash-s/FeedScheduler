from config import get_conf
from redis import Redis


# redis client
_redis = None


def get_redis():
    global _redis
    if _redis:
        return _redis
    else:
        _redis = Redis.from_url(get_conf().redis_url)
        return _redis
