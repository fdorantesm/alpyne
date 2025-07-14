from ..pynversify import Container
from ..adapters.redis_adapter import RedisAdapter


class RedisModule:
    """Registers Redis infrastructure components."""

    def register(self, container: Container):
        container.bind(RedisAdapter).to_self()
