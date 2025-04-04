from peewee import PostgresqlDatabase, DoesNotExist, JOIN
import modules.task.model as task_model
import modules.task.schemas as task_schema
from typing import List
from modules.common.service import ExtenstionService


class TaskService(ExtenstionService):
    table_name = "task"

async def create_task(
    db: PostgresqlDatabase, task_create: task_schema.TaskCreate
) -> task_model.Task:
    task = task_model.Task.create(**task_create.model_dump())
    return task


async def get_tasks_with_done() -> List[task_model.Task]:
    # result = task_model.Task.select(
    #     task_model.Task.id,
    #     task_model.Task.title,
    #     task_model.Task.category,
    #     task_model.Task.status_id,
    #     task_model.Task.staff_id,
    #     task_model.Task.priority_id,
    #     task_model.Task.start_date,
    # ).group_by(task_model.Task.id)
    # return [
    #     (
    #         i.id,
    #         i.title,
    #         i.category,
    #         i.status_id,
    #         i.staff_id,
    #         i.priority_id,
    #         i.start_date,
    #     )
    #     for i in result
    # ]
    return


# .join(done_model.Done, on=(task_model.Task.id == done_model.Done.task_id),join_type=JOIN.LEFT_OUTER)
async def update_task(
    db: PostgresqlDatabase,
    task_create: task_schema.TaskCreate,
    original: task_model.Task,
    task_id: int,
) -> task_model.Task:
    task = task_model.Task.get(task_model.Task.id == task_id)
    task.title = task_create.title if task_create.title else task.title
    task.category = task_create.category if task_create.category else task.category
    task.status_id = task_create.status_id if task_create.status_id else task.status_id
    task.priority_id = (
        task_create.priority_id if task_create.priority_id else task.priority_id
    )
    task.staff_id = task_create.staff_id if task_create.staff_id else task.staff_id
    task.save()
    return task


async def get_task(task_id: int) -> List[task_model.Task] | None:
    result = task_model.Task.select(
        task_model.Task.title,
    ).filter(task_model.Task.id == task_id)
    return [(i.title) for i in result]


async def delete_task(db: PostgresqlDatabase, original: int) -> bool:
    task = task_model.Task.get(task_model.Task.id == original)
    task.delete_instance()
    try:
        task.save()
        return True
    except:
        return False


async def get_task_del(task_id: int) -> List[task_model.Task] | None:
    try:
        task = task_model.Task.get_by_id(task_id)
        return [task]
    except DoesNotExist:
        return None
