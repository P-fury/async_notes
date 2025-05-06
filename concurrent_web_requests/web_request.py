import asyncio

from aiohttp import ClientSession


async def fetch_status(session: ClientSession, url: str)-> int:
    async with session.get(url) as response:
        return response.status



async def main() -> None:
    async with ClientSession() as session:
        url = "http://127.0.0.1:8084"
        status = await fetch_status(session, url)
        print(f"Status for {url}: {status}")


asyncio.run(main())