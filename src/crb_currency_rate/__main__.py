import asyncio

from src.crb_currency_rate.core import load_config
from src.crb_currency_rate.service.dependency import init_dependency
from src.crb_currency_rate.service.parse.tasks import task_currency_rate


async def main() -> None:
    config = load_config()
    init_dependency(config)
    while True:
        await task_currency_rate()  # type: ignore
        await asyncio.sleep(86350)

if __name__ == "__main__":
    asyncio.run(main())
