from cgitb import text
from email.policy import default
from enum import unique
from peewee import AutoField,CharField,BooleanField,ForeignKeyField,IntegerField,PrimaryKeyField,TextField
from db import Base

class Task(Base):
    id = PrimaryKeyField(primary_key=True)
    title = CharField(max_length=1024)
    # due_date = DateField(formats=['%Y-%m-%d'])#formats指定しないとリクエストボディの値を参照しない
    #                                           #その場合、defaultまたは、null=Trueを設定しなければならない（not null Errorが起きる）
    category = TextField(null=False)
    status_id = IntegerField(null=False)
    staff_id = CharField(null=False)
    priority_id = IntegerField(null=False)
    class Meta:
        table_name = "tasks"

class Done(Base):
    task_id = ForeignKeyField(model=Task,primary_key=True,field=Task.id,backref="tasks")
    class Meta:
        table_name = "dones"

class Status(Base):
    id = PrimaryKeyField(primary_key=True,unique=True)
    status_name = TextField(null=False,unique=True)
    class Meta:
        table_name = "status"

class Staff(Base):
    id = PrimaryKeyField(null=False,primary_key=True,unique=True)
    staff_id = CharField(null=False,max_length=6)
    staff_name = TextField(null=False)
    class Meta:
        table_name = "staff"

class Priority(Base):
    id = PrimaryKeyField(null=False)
    importance = TextField(null=False)
    class Meta:
        table_name = "priority"



        
        
        

