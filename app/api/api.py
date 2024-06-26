from fastapi import APIRouter
from app.api.endpoints import pdf
from app.api.endpoints import xlsx

api_router = APIRouter()
api_router.include_router(pdf.router, prefix="/pdf", tags=["pdf"])
api_router.include_router(xlsx.router, prefix="/xlsx", tags=["xlsx"])
