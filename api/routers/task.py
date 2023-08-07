from fastapi import APIRouter

router = APIRouter()


@router.get("/tasks")
async def find_all_tasks():
    pass


@router.post("/tasks")
async def create_task():
    pass


@router.post("/tasks")
async def update_task():
    pass


@router.delete("/tasks")
async def delete_task():
    pass
