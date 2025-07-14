from ..pynversify import Container
from ..adapters.kafka_adapter import KafkaAdapter


class KafkaModule:
    """Registers Kafka infrastructure components."""

    def register(self, container: Container):
        container.bind(KafkaAdapter).to_self()
