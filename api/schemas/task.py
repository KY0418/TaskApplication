from pydantic import BaseModel, ConfigDict,Field

class TaskBase(BaseModel):
    title : str | None = Field(None,json_schema_extra="クリーニングを取りに行く")

class TaskCreate(TaskBase):
    pass

class TaskCreateResponse(TaskCreate):
    id: int

    class ConfigDict:
        from_attributes = True
    #config: ConfigDict = ConfigDict(from_attributes=True)

class Task(TaskBase):
    id : int
    done: bool = Field(default=False,json_schema_extra={"description":"完了フラグ"})
    class ConfigDict:
        from_attributes = True
    #config :ConfigDict = ConfigDict(from_attributes=True)
        



    