from fastapi import FastAPI 
from modules.status.api import router as router_status
from modules.task.api import router as router_task
from modules.done.api import router as router_done
from modules.staff.api import router as router_staff
from modules.importance.api import router  as router_importance
from fastapi.middleware.cors import CORSMiddleware

import logging

logging.getLogger('uvicorn').setLevel(logging.DEBUG)

app = FastAPI(debug=True)

app.add_middleware(
      CORSMiddleware,
      allow_origins = ['http://localhost:3000'],#request元を許可する デプロイ前はドメインを入れる
      allow_methods = ["DELETE","POST","GET","PUT","PATCH"],
      allow_credentials=True,
      allow_headers = ["*"]
  )

routers = [
    router_task,
    router_done,
    router_status,
    router_staff,
    router_importance,
]

for router in routers:
    app.include_router(router)
