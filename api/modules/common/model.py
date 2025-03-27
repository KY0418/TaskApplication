from db import db
from peewee import Model

class ExtentionBaseModel(Model):
  table_name : str
  class Meta:
    database = db
  
  static_columns = []
  def __init__(cls, *args, **kwargs):
      super().__init__(*args, **kwargs)

  @classmethod
  async def find(cls, **kwargs):
    kwargs["fields"] = kwargs.get('fields', cls.static_columns)
    common_query = await cls.wrapper_common_query(**kwargs)
    result = await cls.handle_response(common_query,kwargs.get("fields"))
    return result

  @classmethod
  async def wrapper_common_query(cls,**kwargs):
    fields = [getattr(cls, field) for field in kwargs.get("fields", [])]
    query = cls.select(*fields)
    if kwargs:
      conditions = []
      for key, value in kwargs.items():
        if key in cls.static_columns:
          model_field = getattr(cls, key)
          conditions.append(model_field == value)
      if conditions:
        query = query.where(*conditions)
    return query

  @classmethod
  async def handle_response(cls, result, fields):
    response = []
    for row in result:
      res = {}
      for field in fields:
        res[field] = getattr(row, field)
      response.append(res)
    return response