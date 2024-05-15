from fastapi import FastAPI 
from api.modules.task import RouterTask
from api.modules.done import RouterDone
from fastapi.middleware.cors import CORSMiddleware

import logging

logging.getLogger('uvicorn').setLevel(logging.DEBUG)
app = FastAPI()

app.add_middleware(
      CORSMiddleware,
      allow_origins = ['http://localhost:3000'],
      allow_methods = ["DELETE","POST","GET","PUT"],
      allow_credentials=True,
      allow_headers = ["*"]
  )

app.include_router(RouterTask.router)

app.include_router(RouterDone.router)

