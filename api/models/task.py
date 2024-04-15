from peewee import *

from api.db import Base

db = PostgresqlDatabase("task_data",user="kaneko",password="goldsilver",host="postgresql",port=5432)

class Task(Base):
    __tablename__ = "tasks"

    id = IntegerField(primary_key=True)
    title = CharField(max_length=1024)

    done = DeferredForeignKey(rel_model_name='Done',backref='task',on_delete="CASCADE")
    database = db

class Done(Base):
    __tablename__ = "dones"

    #id = Column(Integer,ForeignKey("tasks.id"),primary_key=True)
    #id = ForeignKeyField(model=Task, field="id",primary_key=True)
    id = IntegerField(primary_key=True)
    task = ForeignKeyField(model=Task,backref="done")
    database = db