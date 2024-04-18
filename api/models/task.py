from peewee import *

from api.db import Base

class Done(Base):
    
    #id = Column(Integer,ForeignKey("tasks.id"),primary_key=True)
    #id = ForeignKeyField(model=Task, field="id",primary_key=True)
    #id = IntegerField(primary_key=True)
    #task = DeferredForeignKey(rel_model_name="Task",backref="done")
    class Meta:
        __tablename__ = "dones"

class Task(Base):
   
    #id = IntegerField(primary_key=True)
    title = CharField(max_length=1024)

    done = BooleanField(default=False, column_name="done")
    class Meta:
        __tablename__ = "tasks"
        
        
        

