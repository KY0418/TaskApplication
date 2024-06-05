from peewee import PostgresqlDatabase
from modules.task.models import Task
from modules.status.models import Status
from modules.staff.models import Staff
from modules.importance.models import Priority
from modules.done.models import Done
import config

#from api.models.task import BaseModel

#DB_URL = "mysql+pymysql://root:@db:3306/demo?charset=utf8"
engine= PostgresqlDatabase(config.DB,user=config.DB_USER,password=config.DB_PASS,port=int(config.DB_PORT),host=config.DB_HOST)
def reset_database():
    engine.drop_tables([Task,Done,Status,Staff,Priority],cascade="CASCADE")
    engine.create_tables([Task,Done,Status,Staff,Priority])

if __name__ == "__main__":
    engine.connect()
    reset_database()
    engine.close()