import asyncio


async def delay(delay_seconds: int) -> int:
    print(f"sleeping for {delay_seconds} seconds")
    await asyncio.sleep(delay_seconds)
    print(f"finished sleeping for {delay_seconds} seconds")
    return delay_seconds


async def hello_every_second():
    for i in range(9):
        await asyncio.sleep(1)
        print("running other code while i am waiting")


async def main()-> None:
    first_delay = asyncio.create_task(delay(3))
    second_delay = asyncio.create_task(delay(4))
    await hello_every_second()
    await first_delay
    await second_delay



asyncio.run(main())