from typing import Optional, Union
from fastapi import APIRouter, Depends
from modules.task.schema import TaskCreateSchema, Task, TaskUpdateSchema
from modules.task.service import TaskService
from db import get_db
from peewee import PostgresqlDatabase
import config as config
from modules.task.model import TaskModel
from modules.common.errors import ErrorCollectionWrapper
from modules.common.schema import response_id_schema, response_bool_schema

db = PostgresqlDatabase(
    config.DB,
    user=config.DB_USER,
    password=config.DB_PASS,
    port=int(config.DB_PORT),
    host=config.DB_HOST,
)

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("")
async def list_tasks(db: PostgresqlDatabase = Depends(get_db)):
    task = await TaskService().get_tasks()
    if task is None:
        ErrorCollectionWrapper().not_found(msg="タスクが存在しません。")
    return task


@router.post("", response_model=Union[response_id_schema, None])
async def create_task(
    payload: TaskCreateSchema, db: PostgresqlDatabase = Depends(get_db)
):
    task_id = await TaskService().create_task(payload)
    return task_id


@router.put("/{task_id}", response_model=response_id_schema)
async def update_task(
    payload: TaskUpdateSchema,
    task_id: int,
    db: PostgresqlDatabase = Depends(get_db),
):
    updated = await TaskService().update_task(payload=payload, id=task_id)
    return response_id_schema(id=updated)


@router.patch("/{task_id}", response_model=response_bool_schema)
async def delete_task(task_id: int, db: PostgresqlDatabase = Depends(get_db)) -> bool:
    await TaskService().soft_delete(task_id=task_id)
    return response_bool_schema(is_successfull=True)
