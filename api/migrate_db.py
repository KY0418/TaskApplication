from peewee import *
from models.task import Task,Done

#from api.models.task import BaseModel

#DB_URL = "mysql+pymysql://root:@db:3306/demo?charset=utf8"
engine= PostgresqlDatabase("task_data",user="kaneko",password="goldsilver",port=5432,host="localhost")

def reset_database():
    engine.drop_tables([Task,Done])
    engine.create_tables([Task,Done])

if __name__ == "__main__":
    engine.connect()
    reset_database()
    engine.close()