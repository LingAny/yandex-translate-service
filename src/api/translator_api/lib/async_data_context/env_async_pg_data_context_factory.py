import os

from . import AsyncDataContextFactory, AsyncPostgresDataContext


class EnvAsyncPostgresDataContextFactory(AsyncDataContextFactory):

    def create(self) -> AsyncPostgresDataContext:

        host = os.environ['DB_HOST']
        port = int(os.environ['DB_PORT'])
        database = os.environ['DB_NAME']
        user = os.environ['DB_USER']
        password = os.environ['DB_PASS']

        return AsyncPostgresDataContext(host, port, database, user, password)
