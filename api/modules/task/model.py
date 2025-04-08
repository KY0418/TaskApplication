from peewee import TextField, AutoField, BooleanField
from modules.common.model import ExtensionBaseModel


class TaskModel(ExtensionBaseModel):
    class Meta:
        table_name = "task"

    id = AutoField(primary_key=True)
    header_title = TextField(null=False)
    active = BooleanField(null=False)

    static_columns = ["id", "header_title", "active"]
