from typing import Optional

from pydantic import BaseModel, Field


# 共通化
class TaskBase(BaseModel):
    title: Optional[str] = Field(None, example="pythonの勉強をする")


class TaskCreate(TaskBase):
    pass


class TaskCreateResponse(TaskCreate):
    id: str

    class Config:
        orm_mode = True


class Task(TaskBase):
    id: str
    done: bool = Field(False, description="完了フラグ")

    class Config:
        orm_mode = True
