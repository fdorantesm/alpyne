import aioredis


class RedisAdapter:
    """Redis adapter with simple connect/close hooks."""

    def __init__(self, url: str = "redis://localhost"):
        self.url = url
        self.redis = None

    async def connect(self):
        self.redis = await aioredis.from_url(self.url)

    async def close(self):
        if self.redis:
            await self.redis.close()
