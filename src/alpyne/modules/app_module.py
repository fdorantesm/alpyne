from ..pynversify import Container
from ..adapters.fastapi_adapter import FastAPIAdapter
from ..adapters.in_memory_provider import InMemoryMessageProvider
from ..use_cases.greet import GreetingService


class AppModule:
    """Registers basic application services and HTTP adapter."""

    def register(self, container: Container):
        container.bind(InMemoryMessageProvider).to_self()
        container.bind(GreetingService).to_factory(
            lambda: GreetingService(container.get(InMemoryMessageProvider))
        )
        container.bind(FastAPIAdapter).to_factory(
            lambda: FastAPIAdapter(container.get(GreetingService))
        )
