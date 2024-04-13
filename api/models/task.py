from peewee import *


from db import BaseModel

class Task(BaseModel):
    __tablename__ = "tasks"

    id = IntegerField(primary_key=True)
    title = CharField(max_length=1024)

    done = ForeignKeyField("Done",backref='task',)

class Done(BaseModel):
    __tablename__ = "dones"

    #id = Column(Integer,ForeignKey("tasks.id"),primary_key=True)
    id = ForeignKeyField(IntegerField(primary_key=True), field='tasks.id')

    task = ForeignKeyField("Task",backref="done")