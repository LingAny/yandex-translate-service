from asyncio import AbstractEventLoop, get_event_loop

from injector import Module, singleton, provider

from translator_api.lib.async_data_context import AsyncDataContext, EnvAsyncPostgresDataContextFactory
from translator_api.lib.async_data_context import EnvAsyncPoolPostgresDataContextFactory


class Configuration(Module):

    # @singleton
    # @provider
    # def provide_routes(self) -> RouteTableDef:
    #     return web.RouteTableDef()

    @singleton
    @provider
    def provide_loop(self) -> AbstractEventLoop:
        return get_event_loop()

    @singleton
    @provider
    def provide_context(self) -> AsyncDataContext:
        return EnvAsyncPoolPostgresDataContextFactory().create()
