from fastapi import HTTPException
from modules.task.model import TaskModel
from modules.task_detail.model import TaskDetailModel
from modules.task.schema import TaskCreateSchema, TaskUpdateSchema
from modules.task_detail.schema import TaskDetailCreateSchema
from modules.common.service import ExtensionService
from modules.common.errors import ErrorCollectionWrapper
from db import db
from peewee import JOIN, fn


class TaskService(ExtensionService):
    table_name = "task"
    model_class = TaskModel

    @classmethod
    async def get_tasks(cls):
        json_fields = fn.json_agg(
            fn.json_build_object(
                "id",
                TaskDetailModel.id,
                "title",
                TaskDetailModel.title,
                "task_id",
                TaskDetailModel.task_id,
                "priority_id",
                TaskDetailModel.priority_id,
                "status_id",
                TaskDetailModel.status_id,
                "staff_id",
                TaskDetailModel.staff_id,
                "created_by",
                TaskDetailModel.created_by,
                "modified_by",
                TaskDetailModel.modified_by,
                "start_date",
                TaskDetailModel.start_date,
                "end_date",
                TaskDetailModel.end_date,
                "is_done",
                TaskDetailModel.is_done,
                "active",
                TaskDetailModel.active,
            )
        ).alias("task_detail")
        result = (
            TaskModel.select(TaskModel, json_fields)
            .join(
                TaskDetailModel, JOIN.INNER, on=TaskModel.id == TaskDetailModel.task_id
            )
            .group_by(TaskModel.id)
            .dicts()
        )
        print(list(result))
        return list(result)

    @classmethod
    async def create_task(cls, payload: TaskCreateSchema):
        task_data = {"header_title": payload.header_title, "active": payload.active}
        with db.atomic():
            try:
                new_task_id = await super()._create(cls.model_class, **task_data)
                task_detail_data = []
                for item in payload.task_detail:
                    data = {
                        "task_id": new_task_id,
                        "title": item.title,
                        "priority_id": item.priority_id,
                        "status_id": item.status_id,
                        "staff_id": item.staff_id,
                        "start_date": item.start_date,
                        "end_date": item.end_date,
                        "active": item.active,
                    }
                    task_detail_data.append(data)
                await cls().validate_duplicate_task_detail(task_detail_data)
                TaskDetailModel.insert_many(task_detail_data).execute()
                return new_task_id
            except HTTPException as e:
                db.rollback()
                raise e
            except Exception as e:
                db.rollback()
                ErrorCollectionWrapper().server_error(msg="システムエラーです。")
                raise e

    @classmethod
    async def validate_duplicate_task_detail(
        cls, payload: list[TaskDetailCreateSchema]
    ):
        for data in payload:
            record = TaskDetailModel.get_or_none(TaskDetailModel.title == data["title"])
            if record is not None:
                ErrorCollectionWrapper().conflicted(msg="そのタスクは既に存在します。")

    @classmethod
    async def is_existance_task(cls, id: int, model: TaskModel | TaskDetailModel):
        record = model.get_or_none(model.id == id)
        if record is None:
            ErrorCollectionWrapper().not_found(msg="そのタスクは存在しません。")

    @classmethod
    async def update_task(cls, payload: TaskUpdateSchema, id: int):
        task_payload = {"header_title": payload.header_title, "active": payload.active}
        task_detail_payload = payload.task_detail
        with db.atomic():
            try:
                cls().is_existance_task(id, TaskModel)
                TaskModel.update(**task_payload).where(TaskModel.id == id).execute()
                for td in task_detail_payload:
                    cls().is_existance_task(id, TaskDetailModel)
                    TaskDetailModel.update(td.dict()).where(
                        TaskDetailModel.id == td.id
                    ).execute()
            except HTTPException as e:
                db.rollback()
                raise e
        return id

    @classmethod
    async def soft_delete(cls, task_id: int) -> bool:
        try:
            cls().is_existance_task(task_id, TaskModel)
            TaskModel.update(active=False).where(TaskModel.id == task_id)
        except HTTPException as e:
            raise e
