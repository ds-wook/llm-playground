from fastapi import APIRouter

from api.routers.creditcard import creditcard_router
from api.routers.post import post_router

index_router = router = APIRouter()


router.include_router(post_router, prefix="/post")
router.include_router(creditcard_router, prefix="/creditcard")
