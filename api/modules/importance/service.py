from peewee import PostgresqlDatabase,DoesNotExist,JOIN
import modules.importance.models as importance_model
import modules.importance.schemas as importane_schema
from typing import List

async def get_importance() -> List[importane_schema.importanceResponse]:
    result = (importance_model.Priority
              .select(
                  importance_model.Priority.id,
                  importance_model.Priority.importance
              ))
    
    return [(i.id,i.importance) for i in result]

async def search_importance(id:int) -> List[importane_schema.importanceResponse]:
    result = (importance_model.Priority
              .select(
                  importance_model.Priority.id,
                  importance_model.Priority.importance
              )
              .filter(importance_model.Priority.id == id))
    return [(i.id,i.importance) for i in result]