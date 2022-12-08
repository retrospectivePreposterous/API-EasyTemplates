def predict (mensajes):
    resultado = []
    for i in mensajes:
        resultado.append(len(i))
    return resultado  
    
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
def predict_get(mensajes: List[str] = Query([])):
    return predict(mensajes)

@app.post("/")
async def predict_post(request: Request):
    data = await request.json()
    return predict_get(**data)
    
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
https://4787-82-159-114-101.ngrok.io/?mensajes=muy bien&mensajes=guay
'''