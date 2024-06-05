from fastapi import APIRouter,Depends,HTTPException
from pydantic import Json
import modules.task.schemas as task_schema
import modules.task.service as task_crud
from db import get_db
from peewee import PostgresqlDatabase
import config

db = PostgresqlDatabase(config.DB,user=config.DB_USER,password=config.DB_PASS,port=int(config.DB_PORT),host=config.DB_HOST)

router = APIRouter()

@router.get("/tasks",response_model=list[task_schema.Task])
async def list_tasks(db: PostgresqlDatabase=Depends(get_db)):
    task = await task_crud.get_tasks_with_done()
    if task is None:
        raise HTTPException(status_code=404,detail="タスクは存在しません")
    task.sort()
    return [ task_schema.Task(id=i[0],title=i[1],category=i[2],status_id=i[3],staff_id=i[4],priority_id=i[5],start_date=i[6])  for i in task]

@router.post("/tasks",response_model=task_schema.TaskCreateResponse)
async def create_task(task_body: task_schema.TaskCreate,db: PostgresqlDatabase=Depends(get_db)):
    task = await task_crud.get_tasks_with_done()
    title = task_body.title
    if task is None:
        raise HTTPException(status_code=404,detail="タスクが存在しません")
    for i in task:
        if i[1] == title:   
            raise HTTPException(status_code=409,detail="タスクは既に存在しています")  
    return  await task_crud.create_task(db,task_body)

@router.put("/tasks/{task_id}")
async def update_task(task_id:int,task_body: task_schema.TaskCreate,db: PostgresqlDatabase=Depends(get_db)):
    # ID検索結果のタイトルを格納している
    task = await task_crud.get_task(task_id=task_id)
    task_check = await task_crud.get_tasks_with_done()
    if task is None:
        raise HTTPException(status_code=404,detail="タスクが存在しません")
    for i in task_check:
        if i[1] == task_body.title and (i[3] !=task_body.status_id or i[2] != task_body.category or i[4] != task_body.staff_id or i[5] != task_body.priority_id):
            break
        elif i[1] == task_body.title:   
            raise HTTPException(status_code=409,detail="タスクは既に存在しています")  
    return await task_crud.update_task(db,task_body,original=task,task_id=task_id)

@router.delete("/tasks/{task_id}", response_model=None)
async def delete_task(task_id: int, db: PostgresqlDatabase=Depends(get_db)):
    task = await task_crud.get_task_del(task_id=task_id)
    # task = None
    if task is None:
        raise HTTPException(status_code=404, detail="タスクは存在しません")

    return await task_crud.delete_task(db, original=task)




