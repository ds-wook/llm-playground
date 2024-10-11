from fastapi import APIRouter

from api.routers.post import post_router

index_router = router = APIRouter()


router.include_router(post_router, prefix="/post")
