from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import api_router
from config import get_app_settings


SETTINGS = get_app_settings()

__version__ = "2022.08"


def create_app() -> FastAPI:
    app = FastAPI(
        title=SETTINGS.PROJECT_NAME,
        version=__version__,
        description=SETTINGS.PROJECT_DESCRIPTION,
        docs_url="/",
    )
    register_cors(app)
    register_routers(app)
    return app


def register_cors(app: FastAPI) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def register_routers(app: FastAPI) -> None:
    app.include_router(api_router)
