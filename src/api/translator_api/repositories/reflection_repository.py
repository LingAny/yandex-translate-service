from uuid import UUID

from injector import inject

from translator_api.entities import RefCodesDTO
from translator_api.lib.async_data_context import AsyncDataContext
from translator_api.lib.entity import create_one


class ReflectionRepository(object):

    @inject
    def __init__(self, context: AsyncDataContext) -> None:
        self._context = context

    async def get_codes_for_reflection(self, reflection_id: UUID) -> RefCodesDTO:
        data = await self._context.callproc(f"get_codes_for_reflection_id($1)", reflection_id)
        entity = create_one(RefCodesDTO, data)
        return entity
