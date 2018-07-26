from translator_api.lib.entity import Entity


class RefCodesDTO(Entity):

    @property
    def _key_field(self) -> str:
        return "reflection_id"

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self._native_code = kwargs['native_code']
        self._foreign_code = kwargs['foreign_code']

    @staticmethod
    def new(native_code: str, foreign_code: str) -> "RefCodesDTO":
        return RefCodesDTO(native_code=native_code,
                           foreign_code=foreign_code)

    @property
    def native_code(self) -> str:
        return self._native_code

    @property
    def foreign_code(self) -> str:
        return self._foreign_code
