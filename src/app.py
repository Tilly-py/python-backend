# -*- coding: utf-8 -*-
from pydantic import BaseModel
from unicorns import storage
from fastapi import FastAPI, Header

class SpottedWhere(BaseModel):
    location: str
    lat: float
    lon: float

class Unicorns(BaseModel):
    id: int
    name: str
    description: str
    reportedBy: str
    spottedWhere: SpottedWhere
    spottedWhen: str
    image: str

app = FastAPI()

@app.get("/")
async def hello():
    return {"Hello": "World!"}

@app.get("/unicorns")
async def get_unicorns(accept: str = Header(default="application/json")):
    print(f"Accept header: {accept}")
    unicorns = storage.fetch_unicorns()
    return unicorns


@app.get("/unicorn/{unicorn_id}")
async def get_unicorn(unicorn_id: int):
    pass

@app.post("/unicorn")
async def create_unicorn():
    pass

@app.put("/unicorn/{unicorn_id}")
async def update_unicorn(unicorn_id: int):
    pass

@app.delete("/unicorn/{unicorn_id}")
async def delete_unicorn(unicorn_id: int):
    pass