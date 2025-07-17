from typing import Type, List

from .container import Container
from ..common.adapters.fastapi_adapter import FastAPIAdapter
from ..common.ports import HttpServer


class AlpyneApplication:
    """Wrapper returned by ``AlpyneFactory.create``."""

    def __init__(self, container: Container, server: HttpServer) -> None:
        self._container = container
        self._server = server

    def get_server(self) -> HttpServer:
        return self._server


class AlpyneFactory:
    """Factory to bootstrap an application from a root module."""

    @staticmethod
    def _collect_controllers(module_cls: Type, container: Container) -> List:
        controllers: List = []
        for ctrl in getattr(module_cls, "controllers", []):
            controllers.append(container.get(ctrl))
        for mod in getattr(module_cls, "imports", []):
            controllers.extend(AlpyneFactory._collect_controllers(mod, container))
        return controllers

    @staticmethod
    def create(
        root_module: Type,
        *,
        description: str | None = None,
        title: str | None = None,
        version: str | None = None,
        debug: bool | None = None,
    ) -> AlpyneApplication:
        container = Container()
        root_module().register(container)
        controllers = AlpyneFactory._collect_controllers(root_module, container)
        server = FastAPIAdapter(
            controllers,
            description=description,
            title=title,
            version=version,
            debug=debug,
        )
        container.bind(HttpServer).to_factory(lambda s=server: s)
        return AlpyneApplication(container, server)
