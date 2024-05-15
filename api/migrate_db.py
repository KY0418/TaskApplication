from peewee import PostgresqlDatabase
from api.modules.task.ModelsTask import Task,Done
import config

#from api.models.task import BaseModel

#DB_URL = "mysql+pymysql://root:@db:3306/demo?charset=utf8"
engine= PostgresqlDatabase(config.DB,user=config.DB_USER,password=config.DB_PASS,port=int(config.DB_PORT),host=config.DB_HOST)
def reset_database():
    engine.drop_tables([Task,Done],cascade="CASCADE")
    engine.create_tables([Task,Done])

if __name__ == "__main__":
    engine.connect()
    reset_database()
    engine.close()