from uuid import UUID

from aiocache import cached
from aiocache.serializers import PickleSerializer
from injector import singleton, inject
from typing import Optional

from translator_api.entities import RefCodesDTO
from translator_api.repositories import ReflectionRepository


@singleton
class ReflectionService(object):

    @inject
    def __init__(self, repo: ReflectionRepository) -> None:
        self._repo = repo

    @cached(key="get_codes_for_reflection", serializer=PickleSerializer())
    async def get_codes_for_reflection(self, reflection_id: UUID) -> Optional[RefCodesDTO]:
        entity = await self._repo.get_codes_for_reflection(reflection_id)
        return entity
