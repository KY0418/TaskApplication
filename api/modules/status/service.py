from peewee import PostgresqlDatabase
import modules.task.models as task_model

async def get_status(task_id: int):
    print(task_id)
    # status_name = task_model.Status.get_or_none(task_model.Status.id == task_id) 
    status_name = (task_model.Status
                   .select(task_model.Status.status_name)
                   .where(task_model.Status.id == task_id))
    print(status_name)
    # if status_name is None: 
    #     return None
    return [(i) for i in status_name]

async def get_status_whole():
    # status_name = task_model.Status.get_or_none(task_model.Status.id == task_id) 
    status = (task_model.Status
                   .select(
                       task_model.Status.id,
                       task_model.Status.status_name))
    # if status_name is None: 
    #     return None

    return [(i.id,i.status_name) for i in status]







    