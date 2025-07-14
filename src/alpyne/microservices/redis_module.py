from ..core.container import Container
from ..core import Module
from ..common.adapters.redis_adapter import RedisAdapter
from ..core.config_service import ConfigService
from ..common.config import RedisConfig
from ..domain.ports import RedisClient


@Module()
class RedisModule:
    """Registers Redis infrastructure components."""

    def register(self, container: Container) -> None:
        cfg_service = container.get(ConfigService)
        redis_cfg: RedisConfig = cfg_service.get("redis")
        container.bind(RedisClient).to_factory(
            lambda c=redis_cfg: RedisAdapter(
                url=c.url,
                service_name=c.service_name,
                username=c.username,
                password=c.password,
            )
        )


