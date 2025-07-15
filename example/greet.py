from alpyne.core import Injectable
from .domain.entities import Greeting
from .domain.ports import MessageProvider


@Injectable
class GreetingService:
    """Application service to obtain greetings."""

    def __init__(self, provider: MessageProvider):
        self._provider = provider

    def get_greeting(self) -> Greeting:
        message = self._provider.get_message()
        return Greeting(message)
