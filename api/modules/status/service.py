from peewee import PostgresqlDatabase
import modules.status.models as status_model

async def get_status(status_id: int):
    status_name = (status_model.Status
                   .select(status_model.Status.status_name)
                   .where(status_model.Status.id == status_id))
    
    return [(i) for i in status_name]

async def get_status_whole():
    status = (status_model.Status
                   .select(
                       status_model.Status.id,
                       status_model.Status.status_name))
    return [(i.id,i.status_name) for i in status]







    