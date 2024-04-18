from peewee import *

from api.db import Base

db = PostgresqlDatabase("task_data",user="kaneko",password="goldsilver",host="postgresql",port=5432)

class Task(Base):
   
    #id = IntegerField(primary_key=True)
    title = CharField(max_length=1024)

    #done = ForeignKeyField(model=Done, on_delete="CASCADE", null=True, backref="task")
    class Meta:
        __tablename__ = "tasks"
        database = db

class Done(Base):
    

    #id = Column(Integer,ForeignKey("tasks.id"),primary_key=True)
    #id = ForeignKeyField(model=Task, field="id",primary_key=True)
    #id = IntegerField(primary_key=True)
    #task = DeferredForeignKey(rel_model_name="Task",backref="done")
    class Meta:
        __tablename__ = "dones"
        database = db
        

