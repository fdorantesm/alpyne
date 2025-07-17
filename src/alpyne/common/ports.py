from abc import ABC, abstractmethod

class HttpServer(ABC):
    """Port for HTTP server adapters."""

    @abstractmethod
    async def start(self) -> None:
        """Start the HTTP server."""
        raise NotImplementedError
