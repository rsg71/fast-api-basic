# main.py

from fastapi import FastAPI


# for request bodies
from typing import Optional
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None




app = FastAPI()

@app.get('/')
async def root():
    return {"message": "Hello World"}


@app.get('/items/{item_id}')
async def read_item(item_id: str):
    return {"item_id": item_id}


@app.post('/items')
async def create_item(item: Item):
    return item
