from fastapi import FastAPI 
from modules.status import RouterStatus
from modules.task import api
from modules.done import RouterDone
from modules.staff import api as stapi
from modules.importance import api as imapi
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

app.include_router(api.router)

app.include_router(RouterDone.router)

app.include_router(RouterStatus.router)

app.include_router(stapi.router)

app.include_router(imapi.router)
