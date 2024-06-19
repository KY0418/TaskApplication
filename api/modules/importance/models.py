from peewee import PrimaryKeyField,TextField,AutoField
from db import Base


class Priority(Base):
    id = AutoField(primary_key=True)
    importance = TextField(null=False)
    class Meta:
        table_name = "priority"