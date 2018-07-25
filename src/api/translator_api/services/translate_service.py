import ujson

import aiohttp
from typing import Optional, Dict, Any, Tuple
from uuid import UUID

import requests
from flask import json
from injector import inject, singleton

from translator_api.entities import WordDTO
from translator_api.services import ReflectionService


@singleton
class TranslateService(object):

    @inject
    def __init__(self, reflection_service: ReflectionService) -> None:
        self._reflection_service = reflection_service
        self._host = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
        self._key = 'trnsl.1.1.20180319T065216Z.ef55a2768a010315.6ad80367b78fed4fc538c3de84288d98d5553e91'

    async def get_translation_by_text(self, text: str, reflection_id: UUID) -> Optional[WordDTO]:

        # need to get data from the web
        codes = await self._reflection_service.get_codes_for_reflection(reflection_id)
        if not codes:
            return None
        translation = await self._translate(text, codes.native_code, codes.foreign_code)
        return WordDTO(uid=None, text=text, translation=translation)

    async def get_text_by_translation(self, translation: str, reflection_id: UUID) -> Optional[WordDTO]:
        codes = await self._reflection_service.get_codes_for_reflection(reflection_id)
        if not codes:
            return None
        text = await self._translate(translation, codes.foreign_code, codes.native_code)
        return WordDTO(uid=None, text=text, translation=translation)

    async def _translate(self, text: str, native_lang_code: str, foreign_lang_code: str) -> str:
        if self._check_if_word_of_phrase(text):
            translation = await self._translate_word(text, native_lang_code, foreign_lang_code)
        else:
            translation = await self._translate_text(text, native_lang_code, foreign_lang_code)
        return translation

    async def _translate_word(self, text, native_language="en", foreign_language="ru") -> Optional[str]:
        parameter = Params(self._key, native_language, foreign_language)
        params = parameter.get_params(text)
        async with aiohttp.ClientSession() as session:
            async with session.get(self._host, params=params, ssl=False, proxy="http://10.100.122.141:3128") as resp:
                data = await resp.json(loads=ujson.loads)
                return None if len(data) == 0 else data.get('text')[0]

    async def _translate_text(self, text, native_language="en", foreign_language="ru") -> Optional[str]:
        parameter = Params(self._key, native_language, foreign_language)
        params, data = parameter.post_params(text)
        response = requests.post(self._host, params=params, data=data)
        data = json.loads(response.text)
        return None if len(data) == 0 else data.get('text')[0]

    @staticmethod
    def _check_if_word_of_phrase(text: str) -> bool:
        text_arr = text.split()
        if len(text_arr) <= 1:
            return True
        else:
            return False


class Params(object):

    def __init__(self, key: str, nlang: str, flang) -> None:
        self._conf_key = key
        self._nlang = nlang
        self._flang = flang

    def get_params(self, text: str) -> Dict[str, Any]:
        lang = self._flang + '-' + self._nlang
        params = {'key': self._conf_key, 'lang': lang, 'text': text}
        return params

    def post_params(self, text: str) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        lang = self._flang + '-' + self._nlang
        params = {'key': self._conf_key, 'lang': lang}
        data = {'text': text}
        return params, data
