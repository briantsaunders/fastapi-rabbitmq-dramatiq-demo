from fastapi import APIRouter

from app import schemas
from app import actors


router = APIRouter()


@router.post("", response_model=schemas.Task)
def create_task(task_in: schemas.TaskCreate):
    actors.run_task.send(task_in.seconds)
    return {"seconds": task_in.seconds, "status": "submitted"}