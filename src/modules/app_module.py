from pynversify import Container
from ..adapters.fastapi_adapter import FastAPIAdapter
from ..use_cases.greet import GreetingService


class AppModule:
    def register(self, container: Container):
        container.bind(GreetingService).to_self()
        container.bind(FastAPIAdapter).to_factory(
            lambda: FastAPIAdapter(container.get(GreetingService))
        )
