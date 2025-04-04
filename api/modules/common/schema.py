from pydantic import BaseModel, ConfigDict

class ExtentionSchema(BaseModel):
  class Schema(BaseModel):
    model_config = ConfigDict(from_attributes=True, validate_assignment=True)

class response_id_schema(BaseModel):
  id: int

class response_bool_schema(BaseModel):
  is_successfull: bool