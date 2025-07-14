import aioredis
from ...domain.ports import RedisClient


class RedisAdapter(RedisClient):
    """Redis adapter with simple connect/close hooks."""

    def __init__(
        self,
        url: str | None,
        service_name: str | None = None,
        username: str | None = None,
        password: str | None = None,
    ) -> None:
        self.url = url
        self.service_name = service_name
        self.username = username
        self.password = password
        self.redis = None

    async def connect(self):
        self.redis = await aioredis.from_url(self.url)

    async def close(self):
        if self.redis:
            await self.redis.close()
