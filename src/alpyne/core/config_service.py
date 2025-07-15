from typing import Any, Callable, Dict


class ConfigService:
    """Simple key-value store for configuration values."""

    def __init__(self) -> None:
        self._values: Dict[str, Any] = {}

    def register(self, name: str, loader: Callable[[], Any]) -> None:
        """Load a configuration section using the provided loader."""
        self.set_section(name, loader())

    def set_section(self, name: str, values: Any) -> None:
        self._values[name] = values

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a value using dot notation (e.g. ``db.user``)."""
        parts = key.split('.')
        current: Any = self._values
        for part in parts:
            if isinstance(current, dict):
                if part in current:
                    current = current[part]
                else:
                    return default
            else:
                if hasattr(current, part):
                    current = getattr(current, part)
                else:
                    return default
        return current


def register_as(
    service: ConfigService, name: str, loader: Callable[[], Any]
) -> None:
    """Register a configuration loader for a section."""
    service.register(name, loader)

