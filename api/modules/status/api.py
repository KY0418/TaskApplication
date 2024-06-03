from typing import List
from fastapi import APIRouter, HTTPException, Depends
from peewee import PostgresqlDatabase
from db import get_db
import modules.status.schemas as status_schema
import modules.status.service as status_crud


router = APIRouter()


@router.get("/tasks/{status_id}/status", response_model=List[status_schema.StatusResponse])
async def status_get(status_id: int, db: PostgresqlDatabase=Depends(get_db)): 
    print(status_id)
    status_name = await status_crud.get_status(task_id=status_id)
    if status_name is None:
        raise HTTPException(status_code=404, detail="Not Found")
    return [res for res in status_name]

@router.get("/tasks/status", response_model=List[status_schema.StatusResponseWhole])
async def status_get_whole( db: PostgresqlDatabase=Depends(get_db)): 
    status_name = await status_crud.get_status_whole()
    if status_name is None:
        raise HTTPException(status_code=404, detail="Not Found")
    return [status_schema.StatusResponseWhole(status_id=res[0],status_name=res[1]) for res in status_name]

