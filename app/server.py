from fastapi import FastAPI

from app.routers.index import index_router

# FastAPI 객체 생성
app = FastAPI(docs_url="/docs", openapi_url="/open-api-docs")

# /api라는 경로로 index_router를 붙인다.
app.include_router(index_router, prefix="/api")


@app.get("/")
async def getHello():
    return "Hello, KaKaoPay!"
