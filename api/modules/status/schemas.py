from pydantic import BaseModel

class StatusResponse(BaseModel):
    status_name : str
    
    class ConfigDict:
        from_attributes = True