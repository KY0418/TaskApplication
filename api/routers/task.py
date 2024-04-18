from re import I, L
from fastapi import APIRouter,Depends,HTTPException
from peewee import *
from api import test
import api.schemas.task as task_schema
import api.cruds.task as task_crud
import api.models.task as task_model
from typing import List
from api.db import get_db

db = PostgresqlDatabase("task_data",user="kaneko",password="goldsilver",host="postgresql",port=5432,autoconnect=True)

router = APIRouter()

@router.get("/tasks",response_model=list[task_schema.Task])
async def list_tasks(db: PostgresqlDatabase=Depends(get_db)):
    test = await task_crud.get_tasks_with_done()
    return [ task_schema.Task(id=i[0],title=i[1],done=i[2])  for i in test]
    #return True
    #return [task_schema.Task(id=1,title="1つ目のタスク",done=False)]

@router.post("/tasks",response_model=task_schema.TaskCreateResponse)
async def create_task(task_body: task_schema.TaskCreate,db: PostgresqlDatabase=Depends(get_db)):
    return  await task_crud.create_task(db,task_body)

@router.put("/tasks/{task_id}")
async def update_task(task_id:int,task_body: task_schema.TaskCreate,db: PostgresqlDatabase=Depends(get_db)):
    task = await task_crud.get_task(task_id=task_id)
    #print(task)
    if task is None:
        raise HTTPException(status_code=404,detail="Task not found")
    
    return task_crud.update_task(db,task_body,original=task,task_id=task_id)

@router.delete("/tasks/{task_id}", response_model=None)
async def delete_task(task_id: int, db: PostgresqlDatabase=Depends(get_db)):
    task = await task_crud.get_task_del(task_id=task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return await task_crud.delete_task(db, original=task)




