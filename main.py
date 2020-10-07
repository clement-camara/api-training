from fastapi import FastAPI
import uvicorn
#import sqlite3
import json

#JSON RESPONSE
from fastapi.responses import JSONResponse


# le app de la  commande unicorn correspond  au app que je definit en dessous comme variable
# main --> nom du fichier
# --reload ---> recharger automatiquement l' api lors d'une modif
# uvicorn main:app --reload

app = FastAPI()

headers = {'Access-Control-Allow-Origin':'*'}


# attention a bien utiliser ce format return pour que le front tape sur l' API
@app.get("/test")
async def test():
  return JSONResponse(content=[{"name":"Test","Value":500},{"name":"Test2","Value":400}], headers=headers)






@app.get("/test2")
async def test2():
  return [{"name":"Test","Value":500},{"name":"Test2","Value":400}]
