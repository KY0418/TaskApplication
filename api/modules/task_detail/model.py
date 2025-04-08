from modules.common.model import ExtensionBaseModel
from peewee import IntegerField,TextField,DateField,AutoField, BooleanField,DateTimeField

class TaskDetailModel(ExtensionBaseModel):
  class Meta:
      table_name = "task_detail"
    
  id = AutoField(primary_key=True)
  task_id = IntegerField(null=False)
  title = TextField(null=False)
  priority_id = IntegerField(null=False)
  status_id = IntegerField(null=False)
  staff_id = IntegerField(null=False)
  created_at = DateTimeField()
  created_by = IntegerField()
  modified_at = DateTimeField()
  modified_by = IntegerField()
  start_date = DateField(null=False)
  end_date = DateField()
  is_done = BooleanField(default=False,null=False)
  active = BooleanField(default=True,null=False)
  
  static_columns = [
     "id",
     "task_id",
     "title",
     "priority_id",
     "status_id",
     "staff_id",
     "created_at",
     "created_by",
     "modified_at",
     "modified_by",
     "start_date",
     "end_date",
     "is_done",
     "active"
  ]

  unique_columns = [
     "title"
  ]
