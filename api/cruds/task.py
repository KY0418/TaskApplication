from asyncio import Task
from copyreg import constructor
from tokenize import String
from peewee import *
import models.task as task_model
import schemas.task as task_schema
from typing import List


async def create_task(db:PostgresqlDatabase,task_create:
                task_schema.TaskCreate) -> task_model.Task:
    #print(f"データベースオブジェクト: {db}")
    task = task_model.Task.create(**task_create.model_dump())
    print(task)
    return task

async def get_tasks_with_done() -> List[task_model.Task]:
    print(task_model.Task.id)
    result = (task_model.Task
             .select(
                task_model.Task.id,
                task_model.Task.title,
                task_model.Task.done,
            )
            .join(task_model.Done, on=(task_model.Task.id == task_model.Done.task_id),join_type=JOIN.LEFT_OUTER)
            #.objects(constructor=task_model.Task)
            .group_by(task_model.Task.id)
    )
    #result = list(result)
    #print(result,"9999")
    #print( [ (i.id,i.title,i.done) for i in result ])
    return [ (i.id,i.title,i.done) for i in result ]

async def update_task(db:PostgresqlDatabase,task_create:task_schema.TaskCreate,
                        original:task_model.Task,task_id:int)-> task_model.Task:
    print(original)
    #task = task_model.Task()
    # task.title = original
    print(task_create)
    task = task_model.Task.get(task_model.Task.id == task_id)
    print(task)
    task.title = task_create
    #task_model.Task.update(title = task_create).where(task_model.Task.id == task_id)
    task.save()
    #task = task_model.Task(title=original)
    return task.title

async def get_task(task_id:int) -> List[task_model.Task] | None:
    result = (task_model.Task.
              select(task_model.Task.title).filter(task_model.Task.id == task_id))
    #result = ResultIterator(result)
    
    return [ (i.title) for i in result ]

async def delete_task(db: PostgresqlDatabase,original: int) -> None:
    task = task_model.Task.get(task_model.Task.id == original)
    task.delete_instance()
    task.save()
    #task_model.Task.delete().where(task_model.Task.id == original)
    #task_model.Task.create_table()

async def get_task_del(task_id:int) -> List[task_model.Task] | None:
    try:
        task = task_model.Task.get_by_id(task_id)
        print(task)
        return [task]
    except DoesNotExist:
        return None
   
