from fastapi import FastAPI
from enum import Enum

"""
Credit: https://medium.com/seaniap/%E5%BF%AB%E9%80%9F%E4%B8%8A%E6%89%8B-%E7%B0%A1%E5%96%AE%E6%98%93%E6%87%82-python%E6%96%B0%E6%89%8B%E7%9A%84fastapi%E4%B9%8B%E6%97%85-ebd09dc0167b
"""

app = FastAPI()

# Predefined Values
class BlogType(str, Enum):
    business = "business"
    story = "story"
    qa = "qa"
    

@app.get("/")
def read_root():
    return {"Hello": "FastAPI"}

# http://127.0.0.1:8000/blog/all?page=2&page_size=10, ? 代表輸入 query parameters，& 分隔兩參數 input
# Query parameters, default values can be set
@app.get("/blog/query")
def get_blogs_all(page=1, page_size=7):
    return {"message": f"blogs： 來自第 {page} 頁， 總共有 {page_size} 筆資料"}

# Note that this needs to be placed before get_blog they share the same prefix
@app.get("/blog/all")
def get_blogs_all():
    return {"message": "所有的 blogs"}

# Path parameter "id", use id:int to specify the acceptable parameters type
@app.get("/blog/{id}")
def get_blog(id:int):
    return {"data":f"Blog 的 id 是：{id}"}

@app.get("/blog/type/{type}")
def get_blog_type(type: BlogType):
    return {"message":f"Blog 的資料型態是 {type}"}



# uvicorn exp1:app --reload