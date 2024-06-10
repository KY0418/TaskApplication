from peewee import PrimaryKeyField,TextField,AutoField
from db import Base


class Priority(Base):
   # id = PrimaryKeyField(primary_key=True,unique=True)
    id = AutoField(primary_key=True)
    importance = TextField(null=False)
    class Meta:
        table_name = "priority"