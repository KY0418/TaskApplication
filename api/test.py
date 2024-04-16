from peewee import *
from pydantic import BaseModel

from typing  import List,Union
engine= PostgresqlDatabase("task_data",user="kaneko",password="goldsilver",host="postgresql",port=5432)

a = engine.connect()
engine.close()
if a == True:
    print("接続エラーなし")

#class change_type(BaseModel):
    #db : PostgresqlDatabase


