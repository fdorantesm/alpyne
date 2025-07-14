from alpyne.core import Module
from alpyne.common.modules.config_module import ConfigModule
from alpyne.microservices.kafka_module import KafkaModule
from alpyne.microservices.redis_module import RedisModule
from .in_memory_provider import InMemoryMessageProvider
from .greet import GreetingService
from .greeting_controller import GreetingController


@Module(
    imports=[ConfigModule, KafkaModule, RedisModule],
    controllers=[GreetingController],
    providers=[InMemoryMessageProvider, GreetingService],
)
class AppModule:
    """Registers basic providers and controllers for the app."""

    pass

