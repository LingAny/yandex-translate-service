from aiohttp import web
from aiohttp.web_app import Application as WebApplication
from injector import inject, singleton

from translator_api.ioc import ioc
from translator_api.routes import TranslateRoute


class Application(object):

    @inject
    def __init__(self) -> None:
        # self._routes: RouteTableDef = ioc.get(RouteTableDef, scope=singleton)
        self._routes = web.RouteTableDef()
        self._translator: TranslateRoute = ioc.get(TranslateRoute, scope=singleton)

    def register(self, app: WebApplication) -> None:
        self._translator.register_routes(self._routes)
        app.add_routes(self._routes)
