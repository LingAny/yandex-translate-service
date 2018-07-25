import logging
import ujson

from aiohttp.web_response import Response
from aiohttp.web_urldispatcher import RouteTableDef
from injector import inject, singleton


@singleton
class TranslateRoute(object):

    @inject
    def __init__(self) -> None:
        self._hello_body = {
            "hello": "hello"
        }

    def register_routes(self, routes: RouteTableDef) -> None:

        @routes.get('/')
        async def hello(request) -> Response:
            return Response(body=ujson.dumps(self._hello_body), content_type='application/json')

        @routes.get('/text/{text}/{ref_id}')
        def _get_translation_by_text(text: str, ref_id: str):
            logging.info(f"text: {text}: ref_id: {ref_id}")
            return Response(text="Hello, world")

        @routes.get('/translation/{translation}/{ref_id}')
        def _get_text_by_translation(translation: str, ref_id: str):
            logging.info(f"translation: {translation}: ref_id: {ref_id}")
            return Response(text="Hello, world")
