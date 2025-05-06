from aiohttp import web
from aiohttp.web_request import Request
from aiohttp.web_response import Response


async def handler(request: Request) -> Response:
    return web.Response(text='Hello, world')

app = web.Application()
app.router.add_route('GET','/', handler)


web.run_app(app, host='127.0.0.1', port=8084)