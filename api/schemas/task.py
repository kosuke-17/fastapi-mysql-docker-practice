from typing import Optional

from pydantic import BaseModel, Field


class Task(BaseModel):
    id: str
    title: Optional[str] = Field(None, example="pythonの勉強をする")
    done: bool = Field(False, description="完了フラグ")
