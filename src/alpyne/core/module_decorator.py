from typing import Iterable, Type, Callable, Any, Dict, List

from fastapi import APIRouter
from .container import Container


def _register_routes(cls: Type, instance: Any) -> None:
    """Attach methods marked with route decorators to ``cls.router``."""
    if getattr(cls, "_routes_registered", False):
        return
    for attr_name in dir(instance):
        method = getattr(instance, attr_name)
        routes: List[Dict[str, Any]] = getattr(method, "__alpyne_routes__", [])
        for route in routes:
            cls.router.add_api_route(
                route["path"],
                method,
                methods=[route["method"].upper()],
                **route.get("opts", {}),
            )
    cls._routes_registered = True


def Route(path: str, *, method: str, **kwargs: Any) -> Callable[[Callable], Callable]:
    """Mark a method as an endpoint."""

    def decorator(func: Callable) -> Callable:
        data = {"path": path, "method": method, "opts": kwargs}
        if hasattr(func, "__alpyne_routes__"):
            func.__alpyne_routes__.append(data)
        else:
            func.__alpyne_routes__ = [data]
        return func

    return decorator


def Get(path: str, **kwargs: Any) -> Callable[[Callable], Callable]:
    return Route(path, method="GET", **kwargs)


def Post(path: str, **kwargs: Any) -> Callable[[Callable], Callable]:
    return Route(path, method="POST", **kwargs)


def Controller(path: str):
    """Decorator to mark a class as a controller with a base path."""

    def decorator(cls: Type) -> Type:
        cls.__alpyne_controller__ = True
        cls.__alpyne_path__ = path
        cls.router = APIRouter(prefix=path)

        original_init = getattr(cls, "__init__", None)

        def __init__(self, *args: Any, **kwargs: Any) -> None:
            if original_init is not None:
                original_init(self, *args, **kwargs)
            else:
                super(cls, self).__init__()  # type: ignore[misc]
            _register_routes(cls, self)

        cls.__init__ = __init__  # type: ignore[assignment]
        return cls

    return decorator


def Injectable(cls: Type) -> Type:
    """Mark a class as injectable."""
    cls.__alpyne_injectable__ = True
    return cls


def Module(*, imports: Iterable[Type] = None, providers: Iterable[Type] = None, controllers: Iterable[Type] = None):
    imports = list(imports or [])
    providers = list(providers or [])
    controllers = list(controllers or [])

    def decorator(cls: Type):
        cls.imports = imports
        cls.providers = providers
        cls.controllers = controllers
        original_register = getattr(cls, "register", None)

        def register(self, container: Container) -> None:
            for mod_cls in cls.imports:
                mod_instance = mod_cls()
                if hasattr(mod_instance, "register"):
                    mod_instance.register(container)
            for dep in cls.providers + cls.controllers:
                container.bind(dep).to_self()
            if original_register:
                original_register(self, container)

        cls.register = register
        return cls

    return decorator

