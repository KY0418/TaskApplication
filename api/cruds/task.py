from peewee import *
import api.models.task as task_model
import api.schemas.task as task_schema

async def create_task(db:PostgresqlDatabase,task_create:
                task_schema.TaskCreate) -> task_model.Task:
    task = task_model.Task(**task_create.dict())
    task.save()
    await db.commit()
    return task

def get_tasks_with_done() -> str:
    # result = (task_model.Task.
    #     Select(
    #         task_model.Task.id,
    #         task_model.Task.title,
    #         ).join(task_model.Done.id == task_model.Task.id).where(task_model.Done.task != None))
    
    #result = list(result)
    print("test")

    return "test"

async def update_task(db:PostgresqlDatabase,task_create:task_schema.TaskCreate,
             original:task_model.Task)-> task_model.Task:
    original.title = task_create.title
    original.update()
    await db.commit()
    db.close()
    return original

async def get_task(task_id:int) -> task_model.Task | None:
    result = (task_model.
              Select(task_model.Task).where(task_model.Task.id == task_id))
    #result = ResultIterator(result)
    
    return result 

#get_taskはresult が返す値を絞り込む必要がある

async def delete_task(db: PostgresqlDatabase,original: task_model.Task) -> None:
    original.delete()
    db.commit()
   
