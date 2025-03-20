from typing import Optional
from peewee import PostgresqlDatabase
from modules.task.models import Task
from modules.status.models import Status
from modules.staff.models import Staff
from modules.importance.models import Priority
from modules.done.models import Done
import config
import click
import importlib.util
import os
from db import db

# sample command: docker exec task_be poetry run python -m migrations.migrate_db

@click.command()
@click.option('--common', is_flag=True)
@click.option('--tbl-name', default=None)
@click.option('--trigger', is_flag=True)
@click.option('--truncate', is_flag=True)
def cli(common: bool, tbl_name: Optional[str], trigger: bool, truncate: bool):
    folder_path = ["migrations/tables"]
    if trigger is True:
        folder_path.append("migrations/triggers")
    for fpath in folder_path:
        for file_name in os.listdir(fpath): 
            if(file_name.endswith(".py")):
                module_name = file_name[:-3]
                if tbl_name is not None: 
                    if module_name == tbl_name:
                        file_path = os.path.join(fpath,file_name)
                else:
                    file_path = os.path.join(fpath,file_name)
                with db.atomic():
                    try:
                        migrate(module_name,file_path)
                        print(f"{fpath}/{file_name} migrate successfully. ")
                    except Exception as e:
                        print(f" file: {fpath}/{file_name}. error: {e}.")
                        db.rollback()    

def migrate(module_name:str,file_path:str):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if hasattr(module, "migrate_up"):
        module.migrate_up()

engine= PostgresqlDatabase(config.DB,user=config.DB_USER,password=config.DB_PASS,port=int(config.DB_PORT),host=config.DB_HOST)
def initialize_importance():
    importance = ["重要度高、緊急度高","重要度高、緊急度低","重要度低、緊急度高","重要度低、緊急度低"]
    status = ["未着手","完了"]
    for i in importance:
        priority = Priority(importance=i)
        priority.save()
    for i in status:
        status_table = Status(status=i)
        status_table.save()
def reset_database():
    engine.drop_tables([Task,Done,Status,Staff,Priority],cascade="CASCADE")
    engine.create_tables([Task,Done,Status,Staff,Priority])

if __name__ == "__main__":
    cli()
    # engine.connect() 
    # reset_database()
    # initialize_importance()
    # engine.close()