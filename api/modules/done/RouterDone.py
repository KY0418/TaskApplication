from typing import List
from fastapi import APIRouter, HTTPException, Depends
from peewee import PostgresqlDatabase
from db import get_db
import api.modules.done.SchemaDone as done_schema
import api.modules.done.ServiceDone as done_crud


router = APIRouter()


@router.put("/tasks/{task_id}/done", response_model=List[done_schema.DoneResponse])
async def mark_task_as_done(task_id: int, db: PostgresqlDatabase=Depends(get_db)): 
    done = await done_crud.get_done(task_id=task_id)
    if done is not None:
        raise HTTPException(status_code=400, detail="Done already exists")
    judge = await done_crud.FLtoTR(task_id)
    if not judge:
        print("Database更新エラー")
    res = await done_crud.create_done(task_id)
    return [res]


@router.delete("/tasks/{task_id}/done", response_model=None)
async def unmark_task_as_done(task_id: int, db: PostgresqlDatabase=Depends(get_db)):
    done = await done_crud.get_done(task_id=task_id)
    if done is None:
        raise HTTPException(status_code=404, detail="Done not found")
    judge = await done_crud.TRtoFL(task_id)
    if not judge:
        print("Database更新エラー")

    return await done_crud.delete_done(original=done)
