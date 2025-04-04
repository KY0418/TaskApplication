
from fastapi import APIRouter,Depends,HTTPException
import modules.importance.schemas as importance_schema
import modules.importance.service as importance_crud
import modules.importance.models as importance_model
from db import get_db
from peewee import PostgresqlDatabase
import config as config

db = PostgresqlDatabase(config.DB,user=config.DB_USER,password=config.DB_PASS,port=int(config.DB_PORT),host=config.DB_HOST)

router = APIRouter(
    prefix='/importance',
)

@router.get("",response_model=list[importance_schema.importanceResponse])
async def list_importances(db:PostgresqlDatabase=Depends(get_db)):
    importance = await importance_crud.get_importance()
    if importance is None:
        raise HTTPException(status_code=404,detaile="Importance Not Found")
    return [importance_schema.importanceResponse(id=i[0],importance=i[1]) for i in importance]
    
@router.get("/{searchid}",response_model=list[importance_schema.importanceResponse])
async def list_importance_search(searchid:int,db:PostgresqlDatabase=Depends(get_db)):
    importance = await importance_crud.search_importance(searchid)
    if importance is None:
        raise HTTPException(status_code=404,detail="Importance Not Found")
    return [importance_schema.importanceResponse(id=i[0],importance=i[1]) for i in importance]