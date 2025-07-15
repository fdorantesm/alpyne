# Alpyne Framework

This repository provides a minimal framework for building Python workers using
Domain Driven Design and Hexagonal Architecture.  It ships with an HTTP
adapter powered by FastAPI, support for Kafka and Redis, a lightweight
dependency‑injection container inspired by `pynversify` and automatic reloads
with `watchgod`.
Alpyne mirrors the NestJS structure: the `core` package provides the
container and configuration service, while `common` hosts reusable
adapters and modules.
Modules declare controllers and providers just like in PyNest. Controllers expose routes while providers implement business logic. Modules group them so they can be easily imported into the container.
The ``@Module`` decorator wires those controllers and providers automatically so each module only lists its classes. Use ``@Controller('/path')`` and ``@Injectable`` on your classes so the framework knows how to treat them. The controller decorator automatically creates a FastAPI ``APIRouter`` using the provided path. Endpoint methods are decorated with ``@Get`` or ``@Post`` to define routes. ``Inject`` can be used as a default value in a constructor parameter to specify the token to resolve. When a module is registered, dependencies are resolved from the built‑in container.

Configuration values are stored in the `ConfigService` which acts as a simple
repository.  Modules declare configuration sections using the `register_as`
function, passing the shared `ConfigService` instance and a loader callback.
Each section is loaded into a typed dataclass (e.g. `KafkaConfig` or
`RedisConfig`). The loaders decide where to read values from
environment variables and modules simply read the
already loaded configuration.

Modules themselves never access environment variables directly. They only
receive typed configuration objects from the `ConfigService`.

### Configuration

`ConfigModule` includes loaders that read environment variables for the
provided modules.  Set the following variables before running the worker:

```
export KAFKA_SERVICE_NAME=my-service
export KAFKA_BOOTSTRAP_SERVERS=broker:9092
export KAFKA_USERNAME=user
export KAFKA_PASSWORD=pass

export REDIS_SERVICE_NAME=my-cache
export REDIS_URL=redis://host:6379
export REDIS_USERNAME=user
export REDIS_PASSWORD=pass
```

The `example` package demonstrates how to build an application on top of the
framework. Run it in development mode with automatic reloads:

```bash
python -m example
```

Ensure all dependencies listed in `pyproject.toml` are installed.

### Creating the server

`PyNestFactory` bootstraps a FastAPI server from the root module. The factory
creates the dependency container internally, collects controllers from your
modules and returns an application object:

```python
from alpyne.core import PyNestFactory
from example.app_module import AppModule

app = PyNestFactory.create(
    AppModule,
    description="This is my Alpyne app",
    title="My App",
    version="1.0.0",
    debug=True,
)
http_server = app.get_server()
```
