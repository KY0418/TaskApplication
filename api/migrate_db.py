
from peewee import PostgresqlDatabase
from modules.task.models import Task
from modules.status.models import Status
from modules.staff.models import Staff
from modules.importance.models import Priority
from modules.done.models import Done
import config

engine= PostgresqlDatabase(config.DB,user=config.DB_USER,password=config.DB_PASS,port=int(config.DB_PORT),host=config.DB_HOST)
def initialize_importance():
    importance = ["重要度高、緊急度高","重要度高、緊急度低","重要度低、緊急度高","重要度低、緊急度低"]
    status = ["未着手","完了","進行中"]
    for i in importance:
        priority = Priority(importance=i)
        priority.save()
    for i in status:
        status_table = Status(status_name=i)
        status_table.save()
def reset_database():
    engine.drop_tables([Task,Done,Status,Staff,Priority],cascade="CASCADE")
    engine.create_tables([Task,Done,Status,Staff,Priority])

if __name__ == "__main__":
    engine.connect()
    reset_database()
    initialize_importance()
    engine.close()