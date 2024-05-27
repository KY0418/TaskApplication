from peewee import PostgresqlDatabase,DoesNotExist,JOIN
from modules import task
import modules.task.models as task_model
import modules.importance.schemas as importane_schema
from typing import List

async def get_importance() -> List[importane_schema.importanceResponse]:
    result = (task_model.Priority
              .select(
                  task_model.Priority.id,
                  task_model.Priority.importance
              ))
    
    return [(i.id,i.importance) for i in result]

async def search_importance(id:int) -> List[importane_schema.importanceResponse]:
    result = (task_model.Priority
              .select(
                  task_model.Priority.id,
                  task_model.Priority.importance
              )
              .filter(task_model.Priority.id == id))
    return [(i.id,i.importance) for i in result]