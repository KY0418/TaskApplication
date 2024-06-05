from peewee import PrimaryKeyField,TextField
from db import Base

class Status(Base):
    id = PrimaryKeyField(primary_key=True,unique=True)
    status_name = TextField(null=False,unique=True)
    class Meta:
        table_name = "status"