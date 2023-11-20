from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class TaskBase(BaseModel):
    title: Optional[str] = Field(None, example="クリーニングを取りに行く")


class Task(TaskBase):
    id: int
    done: bool = Field(False, description="完了フラグ")
    model_config = ConfigDict(from_attributes=True)


class TaskCreate(TaskBase):
    pass


class TaskCreateResponse(TaskCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)
