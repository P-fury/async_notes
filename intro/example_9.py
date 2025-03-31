import asyncio

from intro.util import delay


async def main() -> None:
    long_task = asyncio.create_task(delay(5))

    try:
        result = await asyncio.wait_for(asyncio.shield(long_task), timeout=1)
        print(result)
    except asyncio.TimeoutError:
        print("task took longer than 1 second")
        print(long_task.cancelled())
        result = await long_task
        print(result)


asyncio.run(main())