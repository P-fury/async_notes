import asyncio
from random import randint

from aiohttp import web
from aiohttp.web_request import Request
from aiohttp.web_response import Response

from intro.util import async_timed

@async_timed()
async def handler(request: Request) -> Response:
    delay = randint(1, 10)
    if delay > 7:
        return web.HTTPRequestTimeout()
    await asyncio.sleep(delay)
    return web.Response(text='Hello, world')

app = web.Application()
app.router.add_route('GET','/', handler)


web.run_app(app, host='127.0.0.1', port=8084)