from peewee import CharField,PrimaryKeyField,TextField,AutoField
from db import Base

class Staff(Base):
    # id = PrimaryKeyField(primary_key=True,unique=True)
    id = AutoField(primary_key=True)
    staff_id = CharField(null=False,max_length=6)
    staff_name = TextField(null=False)
    class Meta:
        table_name = "staff"