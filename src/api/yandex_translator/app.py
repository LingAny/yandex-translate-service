import logging

from aiohttp import web

from yandex_translator.application import Application

logging.getLogger().setLevel(logging.DEBUG)

app = web.Application()

application = Application()
application.register(app)

web.run_app(app)
