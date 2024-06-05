from peewee import AutoField,CharField,BooleanField,ForeignKeyField,IntegerField,PrimaryKeyField,TextField,DateField
from db import Base


class Priority(Base):
    id = PrimaryKeyField(null=False)
    importance = TextField(null=False)
    class Meta:
        table_name = "priority"