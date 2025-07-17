from alpyne.core import Controller, Get, Post
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

    @Post("/")
    async def set_greeting(self, message: str):
        self.service.set_greeting(message)
        return {"message": "updated"}
