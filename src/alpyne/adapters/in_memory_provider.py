from ..domain.ports import MessageProvider


class InMemoryMessageProvider(MessageProvider):
    """Simple provider that returns a static message."""

    def __init__(self, message: str = "Hello, World!"):
        self.message = message

    def get_message(self) -> str:
        return self.message
