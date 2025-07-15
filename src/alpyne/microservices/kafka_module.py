from ..core.container import Container
from ..core import Module
from ..common.adapters.kafka_adapter import KafkaAdapter
from ..core.config_service import ConfigService
from ..common.config import KafkaConfig
from ..common.ports import KafkaBroker


@Module()
class KafkaModule:
    """Registers Kafka infrastructure components."""

    def register(self, container: Container) -> None:
        cfg_service = container.get(ConfigService)
        kafka_cfg: KafkaConfig = cfg_service.get("kafka")
        container.bind(KafkaBroker).to_factory(
            lambda c=kafka_cfg: KafkaAdapter(
                bootstrap_servers=c.bootstrap_servers,
                service_name=c.service_name,
                username=c.username,
                password=c.password,
            )
        )


