from peewee import *
from pydantic import BaseModel

from typing  import List,Union
engine= PostgresqlDatabase("task_data",user="kaneko",password="goldsilver",host="postgresql",port=5432)

engine.connect()
a = engine.close()
if a == True:
    print("接続エラーなし")

#class change_type(BaseModel):
    #db : PostgresqlDatabase


