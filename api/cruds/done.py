from peewee import *

import api.models.task as task_model

async def get_done(task_id: int) -> task_model.Done | None:
    result = (task_model.Select(
        task_model.Done).where(task_model.Done.id == task_id)
    )

    return result

async def create_done(db: PostgresqlDatabase,task_id:int) -> task_model.Done:
    done = task_model.Done(id=task_id)
    done.save()
    await db.commit()
    
    return done

async def delete_done(db: PostgresqlDatabase,original:task_model.Done) -> None:
    original.delete()
    await db.commit()
    