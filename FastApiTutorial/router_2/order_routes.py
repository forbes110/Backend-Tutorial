from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional

# 定義 Order 資料模型
class Order(BaseModel):
    id: Optional[int] = None
    item_id: int
    quantity: int

# 建立 order router
order_router = APIRouter()

fake_order_db = {}

@order_router.get("/")
async def get_orders():
    return fake_order_db

@order_router.post("/")
async def create_order(order: Order):
    order_id = len(fake_order_db) + 1
    order.id = order_id
    fake_order_db[order_id] = order.dict()
    return {"message": "訂單已新增", "order": order}
