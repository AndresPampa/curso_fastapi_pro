import os
from supabase import create_client, Client
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
from datetime import datetime
from pydantic import BaseModel
# import random

load_dotenv()
url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
supabase: Client = create_client(url, key)

class Item(BaseModel):
    id: int
    item: str

app = FastAPI()

@app.get("/items")
async def get_data():
    try:
        response = supabase.table("item").select("*").execute()
    except Exception as e:
        raise e
    return JSONResponse(content=response.data, status_code=200)

@app.post("/item")
async def insert_item(item: Item) -> JSONResponse:
    producto_nuevo = {
        "id": item.id,
        "created_at": datetime.now().strftime("%Y-%m-%d"),
        "item": item.item,
    }
    insert = supabase.table("item").insert(producto_nuevo).execute()

    return JSONResponse(content=insert.data, status_code=200)

@app.get("/item/{id}")
async def get_item_by_id(id: int):
    item = supabase.table("item").select("*").eq("id", id).execute()
    return JSONResponse(content=item.data, status_code=200)


@app.put("/item{id}", status_code=status.HTTP_200_OK)
async def update_item(item: Item):
    item_update = supabase.table("item").update({"id":item.id, "item":item.item}).eq("id", item.id).execute()
    return JSONResponse(content=item_update.data, status_code=status.HTTP_200_OK)


@app.delete("/item{id}", status_code=status.HTTP_200_OK)
async def delete_item(id:int):
    item_delete = supabase.table("item").delete().eq("id", id).execute()
    return JSONResponse(content=item_delete.data, status_code=status.HTTP_200_OK)