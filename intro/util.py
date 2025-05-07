# import asyncio
#
# async def delay(delay_seconds: int) -> int:
#     print(f"sleeping for {delay_seconds} seconds")
#     await asyncio.sleep(delay_seconds)
#     print(f"finished sleeping for {delay_seconds} seconds")
#     return delay_seconds
#


import asyncio
import functools
import time
from typing import Callable, Any


async def delay(delay_seconds: int) -> int:
    print(f'sleeping for {delay_seconds} seconds')
    await asyncio.sleep(delay_seconds)
    print(f'finished sleep for {delay_seconds} seconds')
    return delay_seconds


def async_timed() -> Callable:
    def wrapper(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapper(*args: Any, **kwargs: Any) -> Any:
            print(f'starting {func.__name__} with args {args} with kwargs {kwargs}')
            start_time = time.time()
            try:
                result = await func(*args, **kwargs)
                return result
            finally:
                end_time = time.time()
                total_time = end_time - start_time
                print(f'finished in {func.__name__} in {total_time:.4f} seconds')

        return wrapper

    return wrapper
