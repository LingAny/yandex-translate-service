import asyncio
import logging
import uvloop

from aiohttp import web

from translator_api.application import Application

logging.getLogger('aiohttp').setLevel(logging.ERROR)

app = web.Application()

application = Application()
application.register(app)

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

web.run_app(app)
