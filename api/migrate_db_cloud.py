from peewee import *
from api.modules.task.models import Task,Done
from db import Base

#from api.models.task import BaseModel

#DB_URL = "mysql+pymysql://root:@db:3306/demo?charset=utf8"
engine= PostgresqlDatabase("task_data",user="kaneko",password="goldsilver",host="postgresql",port=5432)

def database_exists():
    try:
        engine.connect()
        return True
    except (OperationalError,InternalError) as e:
        print(e)
        print("database does not exist")
        return False

def create_database():
    if not database_exists():
        root = PostgresqlDatabase("task_data",user="kaneko",password="goldsilver",host="postgresql",port=5432)
        confirm = root.connect()
        confirm is not print("check your settings")
    Base.create_table()
    print("created tables")
if __name__ == "__main__":
    engine.connect()

    engine.close()