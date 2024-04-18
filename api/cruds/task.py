from asyncio import Task
from copyreg import constructor
from turtle import title
from fastapi.background import P
from peewee import *
import api.models.task as task_model
import api.schemas.task as task_schema
from typing import List


async def create_task(db:PostgresqlDatabase,task_create:
                task_schema.TaskCreate) -> task_model.Task:
    #print(f"データベースオブジェクト: {db}")
    task = task_model.Task(**task_create.model_dump())
    task.save()
    #print(task)
    return task

async def get_tasks_with_done() -> List[task_model.Task]:
    print(task_model.Task.id)
    result = (task_model.Task
             .select(
                task_model.Task.id,
                task_model.Task.title,
                task_model.Task.done,
            )
            .join(task_model.Done, on=(task_model.Task.id == task_model.Done.id),join_type=JOIN.LEFT_OUTER)
            #.objects(constructor=task_model.Task)
            .group_by(task_model.Task.id)
    )
    #result = list(result)
    #print(result,"9999")
    #print( [ (i.id,i.title,i.done) for i in result ])
    return [ (i.id,i.title,i.done) for i in result ]

async def update_task(db:PostgresqlDatabase,task_create:task_schema.TaskCreate,
                        original:task_model.Task,task_id:int)-> task_model.Task:
    task = task_model.Task.get(task_model.Task.id == task_id)
    task.title = task_create.title
    original = task_create.title
    #task_model.Task.update(title=original).where(task_model.Task.id == task_id)
    #task = task_model.Task(title=original)
    task.save()
    return original

async def get_task(task_id:int) -> List[task_model.Task] | None:
    result = (task_model.Task.
              select(task_model.Task.title).where(task_model.Task.id == task_id))
    #result = ResultIterator(result)
    
    return [ (i.title) for i in result ]

async def delete_task(db: PostgresqlDatabase,original: int) -> None:
    task = task_model.Task.get(task_model.Task.id == original)
    task.delete_instance()
    task.save()
    #task_model.Task.delete().where(task_model.Task.id == original)
    #task_model.Task.create_table()

async def get_task_del(task_id:int) -> List[task_model.Task] | None:
    result = (task_model.Task.
              select(task_model.Task).where(task_model.Task.id == task_id))
    #result = ResultIterator(result)
    
    return [ (i.id) for i in result ]
   
