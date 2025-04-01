import asyncio


async def coroutine_add_one(number: int) -> int:
    return number + 1


def add_one(number: int) -> int:
    return number + 1


async def main():
    result = await coroutine_add_one(1)
    print(result)

asyncio.run(main())