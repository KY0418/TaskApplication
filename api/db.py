from peewee import PostgresqlDatabase,Model
import config

#DB_URL = "mysql+pymysql://root@db:3306/demo?charset=utf8"

db = PostgresqlDatabase(config.DB,user=config.DB_USER,password=config.DB_PASS,port=config.DB_PORT,host=config.DB_HOST)

class Base(Model):
   class Meta:
      database = db

def get_db():
   try:
      db.connect()
      yield
   finally:
      db.close()