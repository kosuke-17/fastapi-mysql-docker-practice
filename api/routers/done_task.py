from fastapi import APIRouter

router = APIRouter()


@router.put("/tasks/{id}/done")
async def mark_as_done_task():
    pass


@router.put("/tasks/{id}/undone")
async def mark_as_undone_task():
    pass
