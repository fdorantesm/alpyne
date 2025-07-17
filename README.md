# Alpyne Framework

This repository provides a minimal framework for building Python workers using
Domain Driven Design and Hexagonal Architecture. It ships with an HTTP adapter
powered by FastAPI, a lightweight dependency‑injection container and automatic
reloads with `watchgod`. Alpyne mirrors the NestJS structure: the `core`
package hosts the container and decorators while `common` contains reusable
adapters.
Modules declare controllers and providers that are grouped into modules. Controllers expose routes while providers implement business logic. Modules group them so they can be easily imported into the container.
The ``@Module`` decorator wires those controllers and providers automatically so each module only lists its classes. A module may specify ``controllers``, ``providers``, other modules through ``imports`` and an ``exports`` list for sharing providers. Use ``@Controller('/path')`` and ``@Injectable`` on your classes so the framework knows how to treat them. The controller decorator automatically creates a FastAPI ``APIRouter`` using the provided path. Endpoint methods are decorated with helpers such as ``@Get`` or ``@Post`` to define routes. All standard HTTP verbs are available, including ``@Put``, ``@Delete``, ``@Patch``, ``@Options`` and ``@Head``. ``Inject`` can be used as a default value in a constructor parameter to specify the token to resolve. When a module is registered, dependencies are resolved from the built‑in container.


The `example` package demonstrates how to build an application on top of the
framework. Run it in development mode with automatic reloads:

```bash
python -m example
```

Ensure all dependencies listed in `pyproject.toml` are installed.

### Creating the server

`AlpyneFactory` bootstraps a FastAPI server from the root module. The factory
creates the dependency container internally, collects controllers from your
modules and returns an application object:

```python
from alpyne.core import AlpyneFactory
from example.app_module import AppModule

app = AlpyneFactory.create(
    AppModule,
    description="This is my Alpyne app",
    title="My App",
    version="1.0.0",
    debug=True,
)
http_server = app.get_server()
```
