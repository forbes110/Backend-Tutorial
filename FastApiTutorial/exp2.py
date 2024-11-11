from fastapi import FastAPI, status, Response
from enum import Enum
import uvicorn


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
@app.get("/blog/query", tags=["query", "blogs"])
def get_blogs_all_haha(page=1, page_size=7):
    return {"message": f"blogs： 來自第 {page} 頁， 總共有 {page_size} 筆資料"}

# Note that this needs to be placed before get_blog they share the same prefix
@app.get(
    "/blog/all", 
    summary="取得所有的 blogs", 
    description="取得所有的 blogs，並且可以指定分頁的資料",
    response_description="所有的 blogs 資料"
)
def get_blogs_all():
    return {"message": "所有的 blogs"}


# Path parameter "id", use id:int to specify the acceptable parameters type
# @app.get("/blog/{id}")
# def get_blog(id:int):
#     return {"data":f"Blog 的 id 是：{id}"}

# this example assumes that only ids below 5 are valid
# add tags to make your API more readable
@app.get("/blog/{id}", tags=["blogs"])
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": f"找不到 Blog 的 id ：{id}"}
    else:
        response.status_code = status.HTTP_200_OK
        return {"message": f"Blog 的 id 是：{id}"}


@app.get("/blog/type/{type}", tags=["type"])
def get_blog_type(type: BlogType):
    return {"message":f"Blog 的資料型態是 {type}"}



# uvicorn exp2:app --reload
# python exp2.py
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
    
    


    
