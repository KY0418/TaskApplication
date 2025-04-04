from modules.common.model import ExtentionBaseModel as EBM

class ExtenstionService():
  table_name: str

  @classmethod
  def find(cls,**kwargs):
    result = EBM.find(**kwargs)
    return result

