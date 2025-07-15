from ...core.container import Container
from ...core.config_service import ConfigService
from ...core import Module


@Module()
class ConfigModule:
    """Registers the ConfigService."""

    def register(self, container: Container) -> None:
        service = ConfigService()
        container.bind(ConfigService).to_factory(lambda s=service: s)
        return

