from fastapi import FastAPI 
from modules.status import api as stateapi
from modules.task import api as api
from modules.done import api as dapi
from modules.staff import api as stapi
from modules.importance import api  as imapi
from fastapi.middleware.cors import CORSMiddleware

import logging

logging.getLogger('uvicorn').setLevel(logging.DEBUG)
app = FastAPI()

app.add_middleware(
      CORSMiddleware,
      allow_origins = ['http://localhost:3000'],#request元を許可する デプロイ前はドメインを入れる
      allow_methods = ["DELETE","POST","GET","PUT"],
      allow_credentials=True,
      allow_headers = ["*"]
  )

app.include_router(api.router)

app.include_router(dapi.router)

app.include_router(stateapi.router)

app.include_router(stapi.router)

app.include_router(imapi.router)
