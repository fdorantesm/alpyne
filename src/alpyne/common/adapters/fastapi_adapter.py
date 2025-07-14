from fastapi import FastAPI
import uvicorn
from typing import Sequence
from ...domain.ports import HttpServer


class FastAPIAdapter(HttpServer):
    """HTTP adapter that mounts controller routers."""

    def __init__(
        self,
        controllers: Sequence,
        *,
        description: str | None = None,
        title: str | None = None,
        version: str | None = None,
        debug: bool | None = None,
    ) -> None:
        self.app = FastAPI(
            description=description,
            title=title,
            version=version,
            debug=debug,
        )
        for controller in controllers:
            # controllers must expose a ``router`` attribute
            self.app.include_router(controller.router)

    async def start(self, host: str = "0.0.0.0", port: int = 8000):
        config = uvicorn.Config(self.app, host=host, port=port)
        server = uvicorn.Server(config)
        await server.serve()
