import asyncio
import datetime
import json
from typing import Awaitable, Dict
from aiohttp import web
from .aliases import BlockingHandler, Handler, MethodHandler, Request, Response


async def time_measurement_async(fun, *args, **kwargs):
    start = datetime.datetime.now()
    data = await fun(*args, **kwargs)
    end = datetime.datetime.now()
    delta = end - start
    return delta.microseconds, data

def time_measurement(fun, *args, **kwargs):
    start = datetime.datetime.now()
    data = fun(*args, **kwargs)
    end = datetime.datetime.now()
    delta = end - start
    return delta.microseconds, data

def load_settings():
    with open('settings.json') as json_file:
        return json.load(json_file)

def post_handler_factory(handler: Handler) -> MethodHandler:
    async def post_handler(request: Request) -> Response:
        if request.content_type != 'application/json':
            raise web.HTTPUnsupportedMediaType
        json_request: Dict = await request.json()
        json_respone: Dict = await handler(json_request)
        return web.json_response(json_respone)
    
    return post_handler

async def get_handler(request: Request) -> Response:
    return web.Response(text="Working...")

def blocking_handler_wrapper(handler: BlockingHandler, executor=None) -> Handler:
    async def non_blocking_handler(request: Dict) -> Dict:
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(executor, handler, request)
    
    return non_blocking_handler

def server(host: str, port: int, handler: Handler) -> None:
    app = web.Application()
    app.add_routes([web.get("/", get_handler), 
                    web.post("/", post_handler_factory(handler))])
    web.run_app(app, host=host, port=port)
