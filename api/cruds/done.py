from peewee import *
from typing import List

import api.models.task as task_model

async def get_done(task_id: int) -> List[task_model.Done] | None:
    result = task_model.Done.get(id = task_id)
    
    return [ i for i in result ] 

async def create_done(db: PostgresqlDatabase,task_id:int) -> task_model.Done:
    done = task_model.Done(id=task_id)
    await done.save()
    
    return done

async def delete_done(db: PostgresqlDatabase,original:task_model.Done) -> None:
    done = task_model.Done.get(id = original)
    done.delete_instance()
    await done.save()
    