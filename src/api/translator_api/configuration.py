from asyncio import AbstractEventLoop, get_event_loop

from aiohttp import web
from aiohttp.web_urldispatcher import RouteTableDef
from injector import Module, singleton, provider


class Configuration(Module):

    @singleton
    @provider
    def provide_context(self) -> RouteTableDef:
        return web.RouteTableDef()

    @singleton
    @provider
    def provide_context(self) -> AbstractEventLoop:
        return get_event_loop()
