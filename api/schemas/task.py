from xmlrpc.client import boolean
from pydantic import BaseModel, ConfigDict,Field
import datetime

class TaskBase(BaseModel):
    title : str | None = Field(None,json_schema_extra="クリーニングを取りに行く")
    due_date: datetime.date | str | None  = Field(None,json_schema_extra="2024-12-01")
    done: bool = Field(None)


class TaskCreate(TaskBase):
    pass

class TaskCreateResponse(TaskCreate):
    id: int

    class ConfigDict:
        from_attributes = True

class Task(TaskBase):
    id : int
    done: bool = Field(default=False,json_schema_extra={"description":"完了フラグ"})
    class ConfigDict:
        from_attributes = True
        



    