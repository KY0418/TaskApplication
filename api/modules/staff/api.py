from fastapi import APIRouter,Depends,HTTPException
import modules.staff.schemas as staff_schema
import modules.staff.service as staff_crud
import modules.task.models as task_model
from db import get_db
from peewee import PostgresqlDatabase
import config


db = PostgresqlDatabase(config.DB,user=config.DB_USER,password=config.DB_PASS,port=int(config.DB_PORT),host=config.DB_HOST)

router = APIRouter()

@router.get("/staffs",response_model=list[staff_schema.StaffResponse])
async def list_staffs(db:PostgresqlDatabase=Depends(get_db)):
    staff = await staff_crud.get_staff()
    if staff is None:
        HTTPException(status_code=404,detail="Staff Not Exist")
    staff.sort()
    return [ staff_schema.StaffResponse(id=i[0],staff_id=i[1],staff_name=i[2])  for i in staff]


@router.post("/staffs",response_model=staff_schema.StaffResponse)
async def create_staff_data(staff_data: staff_schema.StaffRequest,db:PostgresqlDatabase=Depends(get_db)):
    staff = await staff_crud.get_staff()
    st_name = staff_data.staff_name
    if staff is None:
        raise HTTPException(status_code=404 ,detail="Staff Not Exist")
    for i in staff:
        if i[2] == st_name:
            raise HTTPException(status_code=409,detail="Conflict")
    return await staff_crud.regist_staff(db,staff_data)

@router.put("/staffs/{staff_id}")
async def update_staff_data(staff_id:str,staff_data:staff_schema.StaffPutData,db:PostgresqlDatabase=Depends(get_db)):
    staff = await staff_crud.get_staff_for_put(staff_id)
    staff_check = await staff_crud.get_staff()
    st_name = staff_data.staff_name
    if staff is None:
        raise HTTPException(status_code=404,detail="Staff Not Exist")
    for i in staff_check:
        if i[2] == st_name:
            raise HTTPException(status_code=409,detail="Conflict")
    return await staff_crud.update_staff(db,staff_data,staff_id)

@router.delete("/staffs/{staff_id}")
async def delete_staff_data(staff_id:str,db:PostgresqlDatabase=Depends(get_db)):
    staff = await staff_crud.get_staff_for_put(staff_id)
    if staff is None:
        raise HTTPException(status_code=404,detail="Staff Not Exist")

    return await staff_crud.delete_staff_data(staff_id)