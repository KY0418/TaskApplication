from fastapi import FastAPI 
from peewee import *
from routers import task,done

import logging

logging.getLogger('uvicorn').setLevel(logging.DEBUG)
app = FastAPI()
app.include_router(task.router)
app.include_router(done.router)

