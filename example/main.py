import asyncio
from alpyne.core import PyNestFactory
from .app_module import AppModule


async def run() -> None:
    app = PyNestFactory.create(
        AppModule,
        description="Example greeting app",
        title="Greeting App",
        version="1.0.0",
        debug=True,
    )
    http = app.get_server()
    await http.start()


def main() -> None:
    asyncio.run(run())


if __name__ == "__main__":
    main()
