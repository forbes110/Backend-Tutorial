from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional

# 定義 Item 資料模型
class Item(BaseModel):
    id: Optional[int] = None
    name: str
    price: float

# 建立 item router
item_router = APIRouter()

fake_item_db = {}

@item_router.get("/")
async def get_items():
    return fake_item_db

@item_router.post("/")
async def create_item(item: Item):
    item_id = len(fake_item_db) + 1
    item.id = item_id
    fake_item_db[item_id] = item.dict()
    return {"message": "商品已新增", "item": item}
