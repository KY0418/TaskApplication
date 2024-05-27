from pydantic import BaseModel, Field

class StaffRequest(BaseModel):
    staff_name : str

class StaffCreate(StaffRequest):
    staff_id : str = Field(default="000000")
    pass

class StaffPutData(StaffRequest):
    pass

class StaffResponse(StaffCreate):
    id: int
    class ConfigDict:
        from_attributes = True