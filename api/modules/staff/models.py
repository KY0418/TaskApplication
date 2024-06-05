from peewee import CharField,PrimaryKeyField,TextField
from db import Base

class Staff(Base):
    id = PrimaryKeyField(null=False,primary_key=True,unique=True)
    staff_id = CharField(null=False,max_length=6)
    staff_name = TextField(null=False)
    class Meta:
        table_name = "staff"