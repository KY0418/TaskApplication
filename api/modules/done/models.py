from peewee import ForeignKeyField
from modules.task.model import Task
from db import Base


class Done(Base):
    task_id = ForeignKeyField(model=Task,primary_key=True,field=Task.id,backref="tasks")
    class Meta:
        table_name = "dones"