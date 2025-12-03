# -*- coding: utf-8 -*-
from pydantic import BaseModel
from unicorns import storage
from unicorns.Unicorn import Unicorn
from fastapi import FastAPI, Header
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles


# class SpottedWhere(BaseModel):
#     name: str
#     lat: float
#     lon: float

# class Unicorn(BaseModel):
#     name: str
#     description: str
#     reportedBy: str
#     spottedWhere: SpottedWhere
#     spottedWhen: str
#     image: str

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


app.add_middleware(
CORSMiddleware,
allow_origins=["*"],
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"],
)

templates = Jinja2Templates(directory="src/templates")



@app.get("/")
async def get_unicorns(accept: str = Header(default="application/json")):
    print(f"Accept header: {accept}")
    unicorns = storage.fetch_unicorns()
    return unicorns


@app.get("/{unicorn_id}")
async def get_unicorn(unicorn_id: int, accept: str = Header(default="application/json")):
    print(f"Accept header: {accept}")
    unicorn = storage.fetch_unicorn(unicorn_id)
    return unicorn

@app.post("/")
async def create_unicorn(unicorn: Unicorn):
    storage.add_unicorn(unicorn)
    return {"message": "Unicorn created successfully", "unicorn": unicorn}

@app.put("/{unicorn_id}")
async def update_unicorn(unicorn_id: int, new_unicorn: Unicorn):
    old_unicorn = storage.fetch_unicorn(unicorn_id)
    if old_unicorn is None:
        return {"message": "Unicorn not found"}
    new_unicorn.id = unicorn_id
    storage.update_unicorn(new_unicorn)



@app.delete("/{unicorn_id}")
async def delete_unicorn(unicorn_id: int):
    storage.delete_unicorn(unicorn_id)
    return {"message": "Unicorn deleted successfully"}