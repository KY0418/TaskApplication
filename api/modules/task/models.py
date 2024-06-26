from peewee import CharField,IntegerField,TextField,DateField,AutoField
from db import Base

class Task(Base):
    id = AutoField(primary_key=True)
    # id = PrimaryKeyField(primary_key=True) 非推奨になっている
    title = CharField(max_length=1024)
    # due_date = DateField(formats=['%Y-%m-%d'])#formats指定しないとリクエストボディの値を参照しない
    #                                           #その場合、defaultまたは、null=Trueを設定しなければならない（not null Errorが起きる）
    category = TextField(null=False)
    status_id = IntegerField(null=False)
    staff_id = CharField(null=False)
    priority_id = IntegerField(null=False)
    start_date = DateField(null=False,formats=['%Y-%m-%d'])
    class Meta:
        table_name = "tasks"


        
        
        

