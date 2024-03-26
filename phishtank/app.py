from fastapi import FastAPI

from .model import load_phish_data
from .routes import router


def init_app():
    app = FastAPI()

    @app.on_event("startup")
    def startup_event():
        load_phish_data()

    app.include_router(router)

    return app


app = init_app()
