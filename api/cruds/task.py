from asyncio import Task
from copyreg import constructor
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
                task_model.Task.due_date,
            )
            .join(task_model.Done, on=(task_model.Task.id == task_model.Done.task_id),join_type=JOIN.LEFT_OUTER)
            #.objects(constructor=task_model.Task)
            .group_by(task_model.Task.id)
    )
    #result = list(result)
    #print(result,"9999")
    #print( [ (i.id,i.title,i.done) for i in result ])
    return [ (i.id,i.title,i.done,i.due_date) for i in result ]

async def update_task(db:PostgresqlDatabase,task_create:task_schema.TaskCreate,
                        original:task_model.Task,task_id:int)-> task_model.Task:
    print("11111")
    #task = task_model.Task()
    # task.title = original
    print("2222")
    task = task_model.Task.get(task_model.Task.id == task_id)
    print("33333",task)
    task.title = task_create.title
    print("33333",task.title)
    #task_model.Task.update(title = task_create).where(task_model.Task.id == task_id)
    task.save()
    #task = task_model.Task(title=original)
    print("4444")
    return task.title

async def get_task(task_id:int) -> List[task_model.Task] | None:
    result = (task_model.Task.
              select(task_model.Task.title).filter(task_model.Task.id == task_id))
    print(result)
    #result = ResultIterator(result)
    print([ (i.title) for i in result ])
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
   
