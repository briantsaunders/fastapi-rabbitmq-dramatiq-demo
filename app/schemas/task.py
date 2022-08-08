from pydantic import BaseModel, Field


BASE_SCHEMA_EXTRA = {"example": {"seconds": 10}}


class TaskCreate(BaseModel):
    seconds: int = Field(
        title="Duration in seconds the task should run for.", ge=1, le=60
    )

    class Config:
        schema_extra = dict(**BASE_SCHEMA_EXTRA)


class Task(BaseModel):
    seconds: int
    status: str
