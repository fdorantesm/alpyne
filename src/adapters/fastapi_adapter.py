from fastapi import FastAPI
import uvicorn
from ..use_cases.greet import GreetingService


class FastAPIAdapter:
    def __init__(self, greeting_service: GreetingService):
        self.greeting_service = greeting_service
        self.app = FastAPI()
        self.app.get("/")(self.handle_greet)

    async def handle_greet(self):
        return {"message": self.greeting_service.get_message()}

    async def start(self, host: str = "0.0.0.0", port: int = 8000):
        config = uvicorn.Config(self.app, host=host, port=port)
        server = uvicorn.Server(config)
        await server.serve()
