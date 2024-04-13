from peewee import *

#DB_URL = "mysql+pymysql://root@db:3306/demo?charset=utf8"

db = PostgresqlDatabase("task_data",user="kaneko",password="goldsilver",port=5432,host="localhost")

class BaseModel(Model):
   class Meta:
      database = db

def get_db():
   db.connect()