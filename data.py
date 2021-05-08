from collections.abc import MutableSet
from typing import Iterable, Optional
import dependencies
from config import get_conf


class ActiveChannelSet(MutableSet):

    def __init__(self, iterable: Optional[Iterable] = None):
        self.redis = dependencies.get_redis()
        self.redis_set_name = get_conf().redis_channels_set
        if iterable:
            self.redis.sadd(self.redis_set_name, *iterable)

    def __contains__(self, value):
        return bool(self.redis.sismember(self.redis_set_name, value))

    def __iter__(self):
        """

        When one needs a memory friendly solution it is better to use a real iterator but
         as redis SSCAN does not guarantee deduplication,
         the SSCAN implementation can get a little tricky(not impossible).
        """
        return iter([
            member.decode() for member in self.redis.smembers(self.redis_set_name)
        ])

    def __len__(self):
        return int(self.redis.scard(self.redis_set_name))

    def add(self, item):
        self.redis.sadd(self.redis_set_name, item)

    def discard(self, item):
        self.redis.srem(self.redis_set_name, item)
