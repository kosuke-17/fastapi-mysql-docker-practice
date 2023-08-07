from typing import List

from fastapi import APIRouter

import api.schemas.task as task_schema

router = APIRouter()


@router.get("/tasks", response_model=List[task_schema.Task])
async def find_all_tasks():
    taskData = task_schema.Task(id="1", title="pythonの勉強しなきゃ")
    return [taskData]


@router.post("/tasks")
async def create_task():
    pass


@router.post("/tasks")
async def update_task():
    pass


@router.delete("/tasks")
async def delete_task():
    pass
