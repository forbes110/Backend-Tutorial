from fastapi import APIRouter

router = APIRouter(
    prefix="/blog",
    tags=["blogs"],
)

@router.post('/new')
def create_blog():
    pass