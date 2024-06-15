from pydantic import BaseModel, Field

class importanceRequest(BaseModel):
    id : int


class importanceResponse(importanceRequest):
    importance: str
    class ConfigDict:
        from_attributes = True