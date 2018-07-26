from aiohttp import web

from translator_api.app import app


if __name__ == "__main__":
    web.run_app(app)
