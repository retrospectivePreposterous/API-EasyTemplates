# !pip install fastapi pyngrok  uvicorn nest-asyncio 

def substitute (text, tosub):
    return text.replace(tosub, '[SUB]')
    
###################################################    
    
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional, Union, List
from fastapi import FastAPI, HTTPException, Query, Request

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.get("/")
def func_get(text: str, tosub: str  = Query([])):
    return substitute(text, tosub)

@app.post("/")
async def func_post(request: Request):
    data = await request.json()
    return func_get(**data)
    
###################################################  
    
import nest_asyncio
from pyngrok import ngrok
import uvicorn

ngrok_tunnel = ngrok.connect(8000)
print("REST API started")
print("Your public API URL:", ngrok_tunnel.public_url)

nest_asyncio.apply()
uvicorn.run(app, port=8000)


'''
https://4787-82-159-114-101.ngrok.io/?text=chulo&tosub=o
'''