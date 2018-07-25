from typing import Optional
from uuid import UUID

from translator_api.lib.entity import Entity


class WordDTO(Entity):

    @property
    def _key_field(self) -> str:
        return 'word_id'

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self._text = kwargs['text']
        self._translation = kwargs['translation']

    @staticmethod
    def new(uid: Optional[UUID], text: str, translation: str) -> "WordDTO":
        return WordDTO(uid=uid, text=text, translation=translation)

    @property
    def text(self) -> str:
        return self._text

    @property
    def translation(self) -> str:
        return self._translation
