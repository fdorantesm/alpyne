from pynversify import Container
from ..adapters.redis_adapter import RedisAdapter


class RedisModule:
    def register(self, container: Container):
        container.bind(RedisAdapter).to_self()
