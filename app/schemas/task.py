from typing import Union
from uuid import UUID

from pydantic import BaseModel, Field


BASE_SCHEMA_EXTRA = {"example": {"seconds": 10}}


class TaskCreate(BaseModel):
    seconds: int = Field(
        title="Duration in seconds the task should run for.", ge=1, le=300
    )

    class Config:
        schema_extra = dict(**BASE_SCHEMA_EXTRA)


class Task(BaseModel):
    message_id: Union[UUID, None] = None
    seconds: int
    status: str
