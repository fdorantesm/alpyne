import asyncio
from .containers import container
from .adapters.fastapi_adapter import FastAPIAdapter


async def run():
    fastapi = container.get(FastAPIAdapter)
    await fastapi.start()


def main():
    asyncio.run(run())


if __name__ == '__main__':
    main()
