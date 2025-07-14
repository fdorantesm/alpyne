import asyncio
from .container import container
from .adapters.fastapi_adapter import FastAPIAdapter


async def run() -> None:
    http = container.get(FastAPIAdapter)
    await http.start()


def main() -> None:
    asyncio.run(run())


if __name__ == "__main__":
    main()
