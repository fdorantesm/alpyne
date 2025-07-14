from fastapi import FastAPI
import uvicorn
from ..use_cases.greet import GreetingService


class FastAPIAdapter:
    """HTTP adapter exposing GreetingService via FastAPI."""

    def __init__(self, service: GreetingService):
        self.service = service
        self.app = FastAPI()
        self.app.get("/")(self.handle_greet)

    async def handle_greet(self):
        greeting = self.service.get_greeting()
        return {"message": greeting.message}

    async def start(self, host: str = "0.0.0.0", port: int = 8000):
        config = uvicorn.Config(self.app, host=host, port=port)
        server = uvicorn.Server(config)
        await server.serve()
