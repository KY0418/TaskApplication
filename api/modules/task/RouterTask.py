from fastapi import APIRouter,Depends,HTTPException
from pydantic import Json
import api.modules.task.SchemaTask as task_schema
import api.modules.task.ServiceTask as task_crud
import api.modules.task.ModelsTask as task_model
from db import get_db
from peewee import PostgresqlDatabase
import config

db = PostgresqlDatabase(config.DB,user=config.DB_USER,password=config.DB_PASS,port=int(config.DB_PORT),host=config.DB_HOST)

router = APIRouter()

@router.get("/tasks",response_model=list[task_schema.Task])
async def list_tasks(db: PostgresqlDatabase=Depends(get_db)):
    task = await task_crud.get_tasks_with_done()
    if task is None:
        raise HTTPException(status_code=404,detail="Task not found")
    return [ task_schema.Task(id=i[0],title=i[1],done=i[2],due_date=i[3])  for i in task]
    #return True
    #return [task_schema.Task(id=1,title="1つ目のタスク",done=False)]

@router.post("/tasks",response_model=task_schema.TaskCreateResponse)
async def create_task(task_body: task_schema.TaskCreate,db: PostgresqlDatabase=Depends(get_db)):
    task = await task_crud.get_tasks_with_done()
    print(task_body)
    title = task_body.title
    for i in task:
        if i[1] == title:   
            raise HTTPException(status_code=409,detail="Conflict")
    return  await task_crud.create_task(db,task_body)

@router.put("/tasks/{task_id}")
async def update_task(task_id:int,task_body: task_schema.TaskCreate,db: PostgresqlDatabase=Depends(get_db)):
    print("1111")
    task = await task_crud.get_task(task_id=task_id)
    # title = task_body.title
    # done = task_body.done
    print(task_id)
    # for i in task: 
    #     if i[1] == title and i[2] == done:
    #         raise HTTPException(status_code=409,detail="Conflict")
    if task is None:
        print("111")
        raise HTTPException(status_code=404,detail="Task not found")
    return await task_crud.update_task(db,task_body,original=task,task_id=task_id)

@router.delete("/tasks/{task_id}", response_model=None)
async def delete_task(task_id: int, db: PostgresqlDatabase=Depends(get_db)):
    task = await task_crud.get_task_del(task_id=task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return await task_crud.delete_task(db, original=task)




