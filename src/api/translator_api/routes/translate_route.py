import logging
import ujson
from uuid import UUID

from aiohttp.http_exceptions import HttpBadRequest
from aiohttp.web_request import Request
from aiohttp.web_response import Response
from injector import inject, singleton

from translator_api.services import TranslateService


@singleton
class TranslateRoute(object):

    @inject
    def __init__(self, service: TranslateService) -> None:
        self._service = service
        self._hello_body = {
            "hello": "hello"
        }

    def register_routes(self, routes) -> None:

        @routes.get('/text/{text}/{ref_id}')
        async def _get_translation_by_text(request) -> Response:
            try:
                text = request.match_info['text']
                ref_id = request.match_info['ref_id']
                logging.info(f"text: {text}: ref_id: {ref_id}")
                word = await self._service.get_translation_by_text(text=text, reflection_id=UUID(ref_id))
                if not word:
                    return Response(text="no word", status=404)
                body = {
                    'text': word.text,
                    'translation': word.translation
                }
                return Response(status=200, body=ujson.dumps(body))
            except BaseException:
                raise HttpBadRequest(message='bad request')

        @routes.post('/text/')
        async def _get_translation(request: Request) -> Response:
            """
            text на том языке, который изучаем
            """
            try:
                data = await request.json(loads=ujson.loads)
                text = data['data']
                ref_id = data['reflectionId']
                word = await self._service.get_translation_by_text(text=text, reflection_id=UUID(ref_id))
                if not word:
                    return Response(text="no word", status=404)
                body = {
                    'text': word.text,
                    'translation': word.translation
                }
                # logging.error(f"translation: {word.translation}")
                return Response(status=200, body=ujson.dumps(body))
            except BaseException:
                raise HttpBadRequest(message='bad request')

        @routes.post('/translation/')
        async def _get_text(request: Request) -> Response:
            """
            translation на том языке, на котором изучаем
            """
            try:
                data = await request.json(loads=ujson.loads)
                translation = data['data']
                ref_id = data['reflectionId']
                word = await self._service.get_text_by_translation(translation=translation, reflection_id=UUID(ref_id))
                if not word:
                    return Response(text="no word", status=404)
                body = {
                    'text': word.text,
                    'translation': word.translation
                }
                # logging.error(f"text: {word.text}")
                return Response(status=200, body=ujson.dumps(body))
            except BaseException:
                raise HttpBadRequest(message='bad request')
