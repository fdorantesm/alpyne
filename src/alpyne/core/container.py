import inspect
from typing import Any, Callable, Dict


class InjectToken:
    """Wrapper used by ``Inject`` to specify a custom token."""

    def __init__(self, token: Any) -> None:
        self.token = token


def Inject(token: Any) -> InjectToken:
    """Return an ``InjectToken`` instance for constructor defaults."""
    return InjectToken(token)


class Container:
    """Simplified inversion-of-control container inspired by pynversify."""

    def __init__(self) -> None:
        self._providers: Dict[Any, Callable[[], Any]] = {}

    class _Binder:
        def __init__(self, container: "Container", token: Any) -> None:
            self.container = container
            self.token = token

        def to_self(self) -> "Container._Binder":
            cls = self.token
            self.container._providers[self.token] = (
                lambda c=cls: self.container._instantiate(c)
            )
            return self

        def to_factory(self, factory: Callable[[], Any]) -> "Container._Binder":
            self.container._providers[self.token] = factory
            return self

    def bind(self, token: Any) -> "Container._Binder":
        return Container._Binder(self, token)

    def _instantiate(self, cls: type) -> Any:
        sig = inspect.signature(cls)
        kwargs = {}
        for name, param in sig.parameters.items():
            if name == "self":
                continue
            if isinstance(param.default, InjectToken):
                token = param.default.token
            elif param.annotation is not inspect.Parameter.empty:
                token = param.annotation
            else:
                raise TypeError(
                    f"Cannot resolve untyped parameter '{name}' for {cls}"
                )
            kwargs[name] = self.get(token)
        return cls(**kwargs)

    def get(self, token: Any) -> Any:
        provider = self._providers.get(token)
        if provider is None:
            if isinstance(token, type):
                return self._instantiate(token)
            raise KeyError(f"No provider for {token}")
        if isinstance(provider, type):
            return self._instantiate(provider)
        if callable(provider):
            return provider()
        return provider

