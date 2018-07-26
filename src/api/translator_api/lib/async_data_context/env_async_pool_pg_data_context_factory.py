import os
from asyncio import AbstractEventLoop, get_event_loop

from translator_api.lib.async_data_context.async_pool_postgres_data_context import AsyncPoolPostgresDataContext
from . import AsyncDataContextFactory


class EnvAsyncPoolPostgresDataContextFactory(AsyncDataContextFactory):

    def create(self) -> AsyncPoolPostgresDataContext:
        host = os.environ['DB_HOST']
        port = int(os.environ['DB_PORT'])
        database = os.environ['DB_NAME']
        user = os.environ['DB_USER']
        password = os.environ['DB_PASS']
        loop = get_event_loop()

        return AsyncPoolPostgresDataContext(host, port, database, user, password, loop)

    @staticmethod
    def create_with_loop(loop: AbstractEventLoop) -> AsyncPoolPostgresDataContext:

        host = os.environ['DB_HOST']
        port = int(os.environ['DB_PORT'])
        database = os.environ['DB_NAME']
        user = os.environ['DB_USER']
        password = os.environ['DB_PASS']

        return AsyncPoolPostgresDataContext(host, port, database, user, password, loop)
