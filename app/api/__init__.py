from fastapi import APIRouter

from app.api import tasks

api_router = APIRouter()
api_router.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
