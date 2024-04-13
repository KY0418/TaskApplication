from peewee import *

engine= PostgresqlDatabase("task_data",user="kaneko",password="goldsilver",host="postgresql",port=5432)

engine.connect()
a = engine.close()
if a == True:
    print("異常なし")