from peewee import *

#DB_URL = "mysql+pymysql://root@db:3306/demo?charset=utf8"

db = PostgresqlDatabase("task_data",user="kaneko",password="goldsilver",port=5432,host="postgresql")

class Base(Model):
   class Meta:
      database = db

def get_db():
   try:
      db.connect()
      yield
   finally:
      db.close()