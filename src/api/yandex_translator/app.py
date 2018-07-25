import asyncio
import logging
import uvloop

from aiohttp import web

from yandex_translator.application import Application

logging.getLogger().setLevel(logging.DEBUG)

app = web.Application()

application = Application()
application.register(app)

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

web.run_app(app)
