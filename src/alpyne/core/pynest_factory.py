from typing import Type, List

from .container import Container
from ..common.adapters.fastapi_adapter import FastAPIAdapter
from ..domain.ports import HttpServer


class PyNestApplication:
    """Wrapper returned by ``PyNestFactory.create``."""

    def __init__(self, container: Container, server: HttpServer) -> None:
        self._container = container
        self._server = server

    def get_server(self) -> HttpServer:
        return self._server


class PyNestFactory:
    """Factory to bootstrap an application from a root module."""

    @staticmethod
    def _collect_controllers(module_cls: Type, container: Container) -> List:
        controllers: List = []
        for ctrl in getattr(module_cls, "controllers", []):
            controllers.append(container.get(ctrl))
        for imp in getattr(module_cls, "imports", []):
            controllers.extend(PyNestFactory._collect_controllers(imp, container))
        return controllers

    @staticmethod
    def create(
        root_module: Type,
        *,
        description: str | None = None,
        title: str | None = None,
        version: str | None = None,
        debug: bool | None = None,
    ) -> PyNestApplication:
        container = Container()
        root_module().register(container)
        controllers = PyNestFactory._collect_controllers(root_module, container)
        server = FastAPIAdapter(
            controllers,
            description=description,
            title=title,
            version=version,
            debug=debug,
        )
        container.bind(HttpServer).to_factory(lambda s=server: s)
        return PyNestApplication(container, server)
