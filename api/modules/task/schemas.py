from pydantic import Field
from modules.common.schema import ExtentionSchema
from modules.task_detail.schema import TaskDetail

class TaskBase(ExtentionSchema):
    category_id: int
    task_detail: list[TaskDetail]
    active: bool

class TaskUpdate(ExtentionSchema):
    title : str = Field(description="タイトル")
    status_id: int = Field(description="ステータスID")
    priority_id: int = Field(description="優先度ID")
    staff_id: str = Field(description="従業員ID")

class TaskCreate(TaskBase):
    pass

class TaskCreateResponse(TaskCreate):
    id: int | None

    class ConfigDict:
        from_attributes = True

class Task(TaskBase):
    id : int
    