from alpyne.core import Controller, Get
from .greet import GreetingService


@Controller("/greet")
class GreetingController:
    """Controller that exposes GreetingService endpoints."""

    def __init__(self, service: GreetingService) -> None:
        self.service = service

    @Get("/")
    async def get_greeting(self):
        greeting = self.service.get_greeting()
        return {"message": greeting.message}
