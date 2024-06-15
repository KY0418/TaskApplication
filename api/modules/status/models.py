from peewee import PrimaryKeyField,TextField,AutoField
from db import Base

class Status(Base):
    # id = PrimaryKeyField(primary_key=True,unique=True)
    id = AutoField(primary_key=True)
    status_name = TextField(null=False,unique=True)
    class Meta:
        table_name = "status"