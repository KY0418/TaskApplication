from tkinter import NO
from typing import List
from fastapi import APIRouter, HTTPException, Depends
from peewee import *
from api.db import get_db
import api.schemas.done as done_schema
import api.cruds.done as done_crud


router = APIRouter()


@router.put("/tasks/{task_id}/done", response_model=List[done_schema.DoneResponse])
async def mark_task_as_done(task_id: int, db: PostgresqlDatabase=Depends(get_db)):
    print("aaaaaaaaaaaa")
    done = done_crud.get_done(db,task_id=task_id)
    #done = None
    print(done)
    if done is not None:
        print("444")
        raise HTTPException(status_code=400, detail="Done already exists")
    print("777")
    res = await done_crud.create_done(db, task_id)
    print(res)
    #print((done_schema.DoneResponse(id=i[0]) for i in res))
    #return True
    return [res]


@router.delete("/tasks/{task_id}/done", response_model=None)
async def unmark_task_as_done(task_id: int, db: PostgresqlDatabase=Depends(get_db)):
    done = await done_crud.get_done(task_id=task_id)
    if done is None:
        raise HTTPException(status_code=404, detail="Done not found")

    return await done_crud.delete_done(db, original=done)
