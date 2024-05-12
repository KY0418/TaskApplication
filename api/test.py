from peewee import *
# from pydantic import BaseModel
# import cruds.task as task_crud
# from typing  import List,Union
# from fastapi import APIRouter,Depends
# from db import get_db
# import schemas.task as task_schema
engine= PostgresqlDatabase("task_data",user="kaneko",password="goldsilver",host="postgresql",port=5432)

class Tasks(Model):
   
    #id = IntegerField(primary_key=True)
    title = CharField(max_length=1024)

    #done = ForeignKeyField(model=Done, on_delete="CASCADE", null=True, backref="task")
    class Meta:
        __tablename__ = "tas"
        database = engine

a = engine.connect()
engine.create_tables([Tasks])
engine.close()
if a == True:
    print("接続エラーなし")

#class change_type(BaseModel):
    #db : PostgresqlDatabase

# async def create_task(task_body: task_schema.TaskCreate,db: PostgresqlDatabase=Depends(get_db)):
#     try:
#         await task_crud.create_task(db, task_body)
#     except Exception as e:
#         print(f"タスク作成エラー: {e}")
#     return  "test" #await task_crud.create_task(db,task_body)


