from fastapi import APIRouter
from pydantic import BaseModel

class PdfRequest(BaseModel):
    title: str
    content: str

router = APIRouter()

@router.post("/")
async def create_pdf(pdf_request: PdfRequest):
    return {"title": pdf_request.title, "content": pdf_request.content}

@router.get("/")
async def get_pdf():
    return {"message": "Hello, World!"}
