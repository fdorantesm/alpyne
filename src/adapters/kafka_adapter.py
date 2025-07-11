from aiokafka import AIOKafkaProducer, AIOKafkaConsumer


class KafkaAdapter:
    def __init__(self, bootstrap_servers: str = "localhost:9092"):
        self.bootstrap_servers = bootstrap_servers
        self.producer = AIOKafkaProducer(bootstrap_servers=self.bootstrap_servers)
        self.consumer = AIOKafkaConsumer(bootstrap_servers=self.bootstrap_servers)

    async def start(self):
        await self.producer.start()
        await self.consumer.start()

    async def stop(self):
        await self.consumer.stop()
        await self.producer.stop()
