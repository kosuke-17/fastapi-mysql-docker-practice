from fastapi import FastAPI

from api.routers import task, done_task

app = FastAPI()
app.include_router(task.router)
app.include_router(done_task.router)
