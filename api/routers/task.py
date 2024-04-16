from fastapi import APIRouter,Depends,HTTPException
from peewee import *
import api.schemas.task as task_schema
import api.cruds.task as task_crud
import logging
logger = logging.getLogger(__name__)
from api.db import get_db

db = PostgresqlDatabase("task_data",user="kaneko",password="goldsilver",host="postgresql",port=5432,autoconnect=True)

router = APIRouter()

@router.get("/tasks")
async def list_tasks():
    logger.info("test")
    return task_crud.get_tasks_with_done()
    #return True

@router.post("/tasks",response_model=task_schema.TaskCreateResponse)
async def create_task(task_body: task_schema.TaskCreate,db: PostgresqlDatabase=Depends(get_db)):
    return await task_crud.create_task(db,task_body)

@router.put("/tasks/{task_id}")
async def update_task(task_id:int,task_body: task_schema.TaskCreate,db: PostgresqlDatabase=Depends(get_db)):
    task = task_crud.get_task(task_id=task_id)
    if task is None:
        raise HTTPException(status_code=404,detail="Task not found")
    
    return await task_crud.update_task(db,task_body,original=task)

@router.delete("/tasks/{task_id}", response_model=None)
async def delete_task(task_id: int, db: PostgresqlDatabase=Depends(get_db)):
    task = await task_crud.get_task(task_id=task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return await task_crud.delete_task(db, original=task)




