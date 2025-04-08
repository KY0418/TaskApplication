from pydantic import Field
from modules.common.schema import ExtensionSchema
from modules.task_detail.schema import TaskDetailCreateSchema, TaskDetailUpdateSchema


class TaskBase(ExtensionSchema):
    header_title: str
    task_detail: list[TaskDetailCreateSchema]
    active: bool


class TaskUpdateSchema(ExtensionSchema):
    header_title: str = Field(description="タイトル")
    active: bool = Field(description="アクティブ")
    task_detail: list[TaskDetailUpdateSchema]


class TaskCreateSchema(TaskBase):
    pass


class TaskCreateResponse(TaskCreateSchema):
    id: int | None

    class ConfigDict:
        from_attributes = True


class Task(TaskBase):
    id: int
