from fastapi import HTTPException
from peewee import PostgresqlDatabase, DoesNotExist
from modules.task.model import TaskModel
from modules.task_detail.model import TaskDetailModel
from modules.task.schema import TaskCreateSchema
from modules.task_detail.schema import TaskDetailCreateSchema
from typing import List
from modules.common.service import ExtensionService
from modules.common.errors import ErrorCollectionWrapper
from db import db


class TaskService(ExtensionService):
    table_name = "task"
    model_class = TaskModel

    @classmethod
    async def create_task(cls,payload:TaskCreateSchema):
        task_data = {"header_title": payload.header_title,"active": payload.active}
        with db.atomic():
            try:
                new_task_id = await super()._create(cls.model_class,**task_data)
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
                        "active": item.active
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
    async def validate_duplicate_task_detail(cls,payload:list[TaskDetailCreateSchema]):
        for data in payload:
            record = TaskDetailModel.get_or_none(TaskDetailModel.title == data["title"])
            if record is not None:
                ErrorCollectionWrapper().conflicted(msg="そのタスクは既に存在します。")

    @classmethod
    async def update_task(
        task_create: TaskCreateSchema,
        original: TaskModel,
        task_id: int,
    ) -> TaskModel:
        task = TaskModel.get(TaskModel.id == task_id)
        task.title = task_create.title if task_create.title else task.title
        task.category = task_create.category if task_create.category else task.category
        task.status_id = task_create.status_id if task_create.status_id else task.status_id
        task.priority_id = (
            task_create.priority_id if task_create.priority_id else task.priority_id
        )
        task.staff_id = task_create.staff_id if task_create.staff_id else task.staff_id
        task.save()
        return task

    async def get_task(task_id: int) -> List[TaskModel] | None:
        result = TaskModel.select(
            TaskModel.title,
        ).filter(TaskModel.id == task_id)
        return [(i.title) for i in result]


    async def delete_task(db: PostgresqlDatabase, original: int) -> bool:
        task = TaskModel.get(TaskModel.id == original)
        task.delete_instance()
        try:
            task.save()
            return True
        except Exception as e:
            raise e
            return False


    async def get_task_del(task_id: int) -> List[TaskModel] | None:
        try:
            task = TaskModel.get_by_id(task_id)
            return [task]
        except DoesNotExist:
            return None
