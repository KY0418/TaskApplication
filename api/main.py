from fastapi import FastAPI 
# from peewee import *
from routers import task,done
from fastapi.middleware.cors import CORSMiddleware

import logging

logging.getLogger('uvicorn').setLevel(logging.DEBUG)
app = FastAPI()

app.add_middleware(
      CORSMiddleware,
      allow_origins = ['http://localhost:3000'],
      allow_methods = ["DELETE", "POST", "GET","PUT"],
      allow_credentials=True,
      allow_headers = ["*"]
  )

app.include_router(task.router)

app.include_router(done.router)

