from asyncio import AbstractEventLoop

from aiohttp.web_response import Response
from aiohttp.web_urldispatcher import RouteTableDef
from injector import inject


class TranslateRoute(object):

    @inject
    def __init__(self, loop: AbstractEventLoop) -> None:
        self._loop = loop

    def register_routes(self, routes: RouteTableDef) -> None:

        @routes.get('/')
        async def hello(request) -> Response:
            return Response(text="Hello, world")
