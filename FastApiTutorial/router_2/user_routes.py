from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional

# 定義 User 資料模型
class User(BaseModel):
    id: Optional[int] = None
    name: str
    email: str

# 建立 user router
user_router = APIRouter()

fake_user_db = {}

@user_router.get("/")
async def get_users():
    return fake_user_db

@user_router.post("/")
async def create_user(user: User):
    user_id = len(fake_user_db) + 1
    user.id = user_id
    fake_user_db[user_id] = user.dict()
    return {"message": "使用者已新增", "user": user}
