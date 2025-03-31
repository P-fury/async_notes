import asyncio

from util import delay  # type: ignore


async def main() -> None:
    long_task = asyncio.create_task(delay(10))

    try:
        result = await asyncio.wait_for(long_task, timeout=6)
        print(result)
    except asyncio.TimeoutError:
        print("timed out")
        print(long_task.cancelled())
    seconds_elapsed = 0

    while not long_task.done():
        print("task not finished")
        await asyncio.sleep(1)
        seconds_elapsed += 1
        if seconds_elapsed > 5:
            long_task.cancel()

    try:
        await long_task
    except asyncio.CancelledError:
        print('cancelled')


asyncio.run(main())
