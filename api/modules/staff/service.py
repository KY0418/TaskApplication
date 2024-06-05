from peewee import PostgresqlDatabase,DoesNotExist,JOIN
import modules.staff.models as staff_model
import modules.staff.schemas as staff_schema
from typing import List


async def get_staff() -> List[staff_schema.StaffResponse]:
    result = (staff_model.Staff
              .select(
                  staff_model.Staff.id,
                  staff_model.Staff.staff_id,
                  staff_model.Staff.staff_name
              ))
    
    return [(i.id,i.staff_id,i.staff_name) for i in result]


async def search_staff(st_id:str) -> List[staff_schema.StaffRequest]:
    result = (staff_model.Staff
              .select(
                  staff_model.Staff.id,
                  staff_model.Staff.staff_id,
                  staff_model.Staff.staff_name
              ).filter(staff_model.Staff.staff_id == st_id ))

    return [(i.staff_name) for i in result]

async def regist_staff(db:PostgresqlDatabase,staff_data:staff_schema.StaffRequest) -> staff_model.Staff:
    res = await get_staff()
    compList = []
    for i in res:
        compList.append(i[0])
    if not compList:
        compList.append(0)
    swap = str(max(compList)+1).zfill(6)
    create_data = staff_schema.StaffCreate(staff_id=str(swap),staff_name=staff_data.staff_name)
    staff = staff_model.Staff.create(**create_data.model_dump())

    return staff

async def update_staff(db:PostgresqlDatabase,staff_regist:staff_schema.StaffPutData,
                       staff_id:str) -> List[staff_model.Staff]:
    staff = staff_model.Staff.get(staff_model.Staff.staff_id == staff_id)
    staff.staff_name = staff_regist.staff_name
    staff.save()

    return [staff.staff_id,staff.staff_name]

async def get_staff_for_put(staff_id:str) -> List[staff_model.Staff] | None:
    result = (staff_model.Staff
                .select(staff_model.Staff.staff_id,
                      staff_model.Staff.staff_name)
                .where(staff_model.Staff.staff_id == staff_id))
    return [(i.staff_name) for i in result]

async def delete_staff_data(staff_id:str):
    staff = staff_model.Staff.get(staff_model.Staff.staff_id ==staff_id)
    if staff is None:
        return False
    staff.delete_instance()
    staff.save()

    return True

