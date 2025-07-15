from aiokafka import AIOKafkaProducer, AIOKafkaConsumer
from ..ports import KafkaBroker


class KafkaAdapter(KafkaBroker):
    """Kafka adapter providing start/stop lifecycle hooks."""

    def __init__(
        self,
        bootstrap_servers: str | None,
        service_name: str | None = None,
        username: str | None = None,
        password: str | None = None,
    ) -> None:
        self.bootstrap_servers = bootstrap_servers
        self.service_name = service_name
        self.username = username
        self.password = password
        self.producer = AIOKafkaProducer(bootstrap_servers=self.bootstrap_servers)
        self.consumer = AIOKafkaConsumer(bootstrap_servers=self.bootstrap_servers)

    async def start(self):
        await self.producer.start()
        await self.consumer.start()

    async def stop(self):
        await self.consumer.stop()
        await self.producer.stop()
