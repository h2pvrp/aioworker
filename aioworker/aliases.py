from typing import Awaitable, Callable, Dict
from aiohttp import web


BlockingHandler = Callable[[Dict], Dict]
Handler = Callable[[Dict], Awaitable[Dict]]
Request = web.BaseRequest
Response = web.Response
MethodHandler = Callable[[Request], Awaitable[Response]]
