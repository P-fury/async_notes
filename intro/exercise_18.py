import asyncio

from intro.util import delay


def call_later():
    print('calling in future')


async def main():
    loop = asyncio.get_running_loop()
    loop.call_soon(call_later)
    # d5 = asyncio.create_task(delay(5))
    # d2 = asyncio.create_task(delay(2))

    await delay(3)
    await delay(2)


async def  magic() -> None:
    await main()

asyncio.run(main())