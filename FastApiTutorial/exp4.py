from fastapi import FastAPI
from router_2.user_routes import user_router
from router_2.item_routes import item_router
from router_2.order_routes import order_router

app = FastAPI()

"""
Now splits by services
"""

# 包含 routers 並設置不同的前綴
app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(item_router, prefix="/items", tags=["Items"])
app.include_router(order_router, prefix="/orders", tags=["Orders"])

@app.get("/")
async def root():
    return {"message": "歡迎來到我的 API"}

# lsof -i :8000
# kill -9 <PID>