from peewee import *
import api.modules.task.ModelsTask as task_model

async def get_done(task_id: int):
    print(task_id)
    done = task_model.Done.get_or_none(task_model.Done.task_id == task_id) 
    print(done)
    if done is None: 
        return None
    return done


async def create_done(id:int) -> task_model.Done:
    done = task_model.Done.create(task_id = id)
    
    return done.task_id

async def delete_done(original:task_model.Done) -> None:
    done = task_model.Done.get(task_model.Done.task_id == original)
    print(done)
    done.delete_instance()

async def FLtoTR(task_id:int) -> bool:
    result = task_model.Task.get(task_model.Task.id == task_id)
    print(result)
    result.done = True
    try:
        result.save()
    except:
        return False
    return True

async def TRtoFL(task_id) -> bool:
    result = task_model.Task.get(task_model.Task.id == task_id)
    print(result)
    result.done = False
    try:
        result.save()
    except:
        return False
    return True



    