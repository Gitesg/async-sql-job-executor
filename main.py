from fastapi import FastAPI
from w1 import execute_sql, t
from celery.result import AsyncResult

app = FastAPI()


@app.get("/run-task")
def run_task():
    task = execute_sql.delay()
    return {"task_id": task.id}


@app.get("/task-status/{task_id}")
def task_status(task_id: str):
    async_result = AsyncResult(task_id, app=t)
    return {
        "task_id": task_id,
        "status": async_result.status,
        "result": async_result.result if async_result.ready() else None
    }
