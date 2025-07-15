from abc import ABC, abstractmethod


class HttpServer(ABC):
    """Port for HTTP server adapters."""

    @abstractmethod
    async def start(self) -> None:
        """Start the HTTP server."""
        raise NotImplementedError


class KafkaBroker(ABC):
    """Port for Kafka broker adapters."""

    @abstractmethod
    async def start(self) -> None:
        """Start the broker."""
        raise NotImplementedError

    @abstractmethod
    async def stop(self) -> None:
        """Stop the broker."""
        raise NotImplementedError


class RedisClient(ABC):
    """Port for Redis adapters."""

    @abstractmethod
    async def connect(self) -> None:
        """Establish the connection."""
        raise NotImplementedError

    @abstractmethod
    async def close(self) -> None:
        """Close the connection."""
        raise NotImplementedError

