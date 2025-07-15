from alpyne.core import Module
from .in_memory_provider import InMemoryMessageProvider
from .greet import GreetingService
from .greeting_controller import GreetingController


@Module(
    controllers=[GreetingController],
    providers=[InMemoryMessageProvider, GreetingService],
)
class AppModule:
    """Registers basic providers and controllers for the app."""

    pass

