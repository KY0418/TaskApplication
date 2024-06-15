from peewee import PostgresqlDatabase
from modules.done.models import Done as task_model
from modules.done.models import Done as task_model

async def get_done(task_id: int):
    done = task_model.get_or_none(task_model.task_id == task_id) 
    if done is None: 
        return None
    return done


async def create_done(id:int) -> task_model:
    done = task_model.create(task_id = id)
    
    return done.task_id

async def delete_done(original:task_model) -> None:
    done = task_model.get(task_model.task_id == original)

    done.delete_instance()

async def FLtoTR(task_id:int) -> bool:
    result = task_model.Task.get(task_model.Task.id == task_id)
    result.done = True
    try:
        result.save()
    except:
        return False
    return True

async def TRtoFL(task_id) -> bool:
    result = task_model.Task.get(task_model.Task.id == task_id)
    result.done = False
    try:
        result.save()
    except:
        return False
    return True



    