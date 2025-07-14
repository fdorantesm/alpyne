from .pynversify import Container
from .modules.app_module import AppModule
from .modules.kafka_module import KafkaModule
from .modules.redis_module import RedisModule


container = Container()


def load_default_modules() -> None:
    """Register the default framework modules."""
    AppModule().register(container)
    KafkaModule().register(container)
    RedisModule().register(container)


load_default_modules()
