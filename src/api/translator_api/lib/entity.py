import copy

from abc import abstractmethod
from typing import Any, Dict, Type, List, TypeVar, Optional

T = TypeVar('T', bound="Entity")


def create_one(cls: Type[T], data: List[Dict[str, Any]]) -> Optional[T]:
    if not data:
        return None
    return cls.create(data[0])


def create_many(cls: Type[T], data: List[Dict[str, Any]]) -> List[T]:
    entities = []
    for row in data:
        entities.append(cls.create(row))
    return entities


class Entity(object):

    def __init__(self, **kwargs) -> None:
        self._uid = kwargs.get('uid') or kwargs.get(self._key_field)

    @property
    @abstractmethod
    def _key_field(self) -> str:
        raise NotImplementedError

    @property
    def uid(self) -> Any:
        return self._uid

    @classmethod
    def create(cls: Type[T], values: Dict[str, Any]) -> T:
        # noinspection PyCallingNonCallable
        entity = cls(**values)  # type: ignore
        return entity

    def copy(self: T) -> T:
        entity = copy.deepcopy(self)
        return entity

    def set_new_id(self, uid: Any) -> None:
        if self.uid:
            raise AttributeError("Id already set")
        self._uid = uid
