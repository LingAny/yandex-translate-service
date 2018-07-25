from abc import ABCMeta, abstractmethod
from typing import List, Any, Dict


class AsyncDataContext(metaclass=ABCMeta):

    @property
    @abstractmethod
    def conn_string(self) -> str:
        return NotImplemented

    @abstractmethod
    async def callproc(self, cmd: str, *args) -> List[Dict[str, Any]]:
        return NotImplemented
