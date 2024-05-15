from email.policy import default
from enum import unique
from peewee import AutoField,CharField,BooleanField,ForeignKeyField,DateField
from db import Base

class Task(Base):
    id = AutoField(primary_key=True)
    title = CharField(max_length=1024)
    due_date = DateField(formats=['%Y-%m-%d'])#formats指定しないとリクエストボディの値を参照しない
                                              #その場合、defaultまたは、null=Trueを設定しなければならない（not null Errorが起きる）
    done = BooleanField(default=False, column_name="done")
    # category = CharField(null=false,unique=true)
    # staus_id = IntegerField(null=false)
    class Meta:
        table_name = "tasks"

class Done(Base):
    task_id = ForeignKeyField(model=Task,primary_key=True,field=Task.id,backref="tasks")
    #id = ForeignKeyField(model=Task, field="id",primary_key=True)
    #id = IntegerField(primary_key=True)
    #task = DeferredForeignKey(rel_model_name="Task",backref="done")
    class Meta:
        table_name = "dones"

# class Status(Base):
#     id = ForeignKeyField(model=Task,primary_key=True,field=Task.staus_id,backref="tasks")
#     status_name = CharField(null=false,default="未完")
#     class Meta:
#         table_name = "status"


        
        
        

