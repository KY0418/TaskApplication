from pydantic import BaseModel

class StatusResponse(BaseModel):
    status_name : str
    
    class ConfigDict:
        from_attributes = True

class StatusResponseWhole(BaseModel):
    status_id: int
    status_name:str

    class ConfigDict:
        from_attributes = True