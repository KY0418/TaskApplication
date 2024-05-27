from pydantic import BaseModel,Field
import datetime

class TaskBase(BaseModel):
    title : str | None = Field(None)
    # due_date: datetime.date | str | None  = Field(None)
    category: str = Field(None)
    status_id: int = Field(None)
    staff_id: str = Field(None)
    priority_id: int = Field(None)

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
    