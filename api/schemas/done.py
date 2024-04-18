from typing import ClassVar
from pydantic import BaseModel, ConfigDict

class DoneResponse(BaseModel):
    id : int
    
    class ConfigDict:
        from_attributes = True
        