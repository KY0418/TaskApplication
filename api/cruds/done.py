from asyncio import Task
from turtle import done
from peewee import *
from typing import List

import api.models.task as task_model

# async def get_done(db,task_id: int) -> task_model.Done | None:
#     # result = (task_model.Task
#     #           .select(task_model.Task.done)
#     #           .where((task_model.Task.done == False) & (task_model.Task.id == task_id)))
#     result = (task_model.Task
#               .select(task_model.Task.done)
#               .where((task_model.Task.id == task_id) & (task_model.Task.done == False)))   
#     #result = task_model.Done.get(id = task_id)
#     print(result)
#     res = result.limit(1).get()
#     #return [(i.done) for i in result]
#     print(res)
#     return res

async def get_done(db,task_id: int) :
    done = task_model.Done.get_or_none(task_model.Done.id == task_id) 
    print(done)
    return done


async def create_done(db: PostgresqlDatabase,task_id:int) -> List[task_model.Done]:
    done = task_model.Done(task_id)
    done.save()
    #res = (task_model.Done.select(task_model.Done.id).where(task_model.Done.id == task_id))
    return [done] 

async def delete_done(db: PostgresqlDatabase,original:task_model.Done) -> None:
    done = task_model.Done.get(id = original)
    done.delete_instance()
    await done.save()
    