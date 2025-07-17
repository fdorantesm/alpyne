from abc import ABC, abstractmethod


class MessageProvider(ABC):
    """Port for retrieving greeting messages."""

    @abstractmethod
    def get_message(self) -> str:
        """Return a greeting message."""
        raise NotImplementedError

    @abstractmethod
    def set_message(self, message: str) -> None:
        """Persist a greeting message."""
        raise NotImplementedError
