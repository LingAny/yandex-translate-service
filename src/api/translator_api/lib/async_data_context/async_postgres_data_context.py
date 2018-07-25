from typing import List, Any, Dict

import asyncpg
from asyncpg import Connection, UniqueViolationError, \
    RestrictViolationError, NotNullViolationError, ForeignKeyViolationError, NoDataFoundError

from . import AsyncDataContext

from .errors import UniqueViolationError as ApiUniqueViolationError
from .errors import NoDataFoundError as ApiNoDataFoundError
from .errors import ForeignKeyViolationError as ApiForeignKeyViolationError
from .errors import RestrictViolationError as ApiRestrictViolationError


class AsyncPostgresDataContext(AsyncDataContext):

    @property
    def conn_string(self) -> str:
        return f'postgres://{self._user}:{self._password}@{self._host}:{self._port}/{self._database}'

    def __init__(self, host: str, port: int, database: str, user: str, password: str) -> None:
        self._host = host
        self._port = port
        self._database = database
        self._user = user
        self._password = password

    async def callproc(self, cmd: str, *args) -> List[Dict[str, Any]]:
        conn = await self.create_connection()
        try:
            return await conn.fetch(f'SELECT * FROM {cmd};', *args)
        except UniqueViolationError:
            raise ApiUniqueViolationError
        except ForeignKeyViolationError:
            raise ApiForeignKeyViolationError
        except RestrictViolationError:
            raise ApiRestrictViolationError
        except NotNullViolationError:
            raise ApiRestrictViolationError
        except NoDataFoundError:
            raise ApiNoDataFoundError
        finally:
            await conn.close()

    async def create_connection(self) -> Connection:
        return await asyncpg.connect(self.conn_string)
