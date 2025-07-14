from dataclasses import dataclass
from typing import Optional


@dataclass
class KafkaConfig:
    service_name: str
    bootstrap_servers: str
    username: Optional[str] = None
    password: Optional[str] = None


@dataclass
class RedisConfig:
    service_name: str
    url: str
    username: Optional[str] = None
    password: Optional[str] = None


