from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import JSONResponse
from app.adapters import entry_adapter

router = APIRouter()

# create endpoint - recieve a raw json from body
@router.post("/")
async def create_pdf(request: Request): 
    json_data = await request.json()

    # comprobate if json_data is a list and response a 422 status code if not
    if not isinstance(json_data, list):
        raise HTTPException(status_code=422, detail="JSON data must be a list")
    
    # comprobate if not empty
    if not json_data:
        raise HTTPException(status_code=422, detail="JSON data is empty")

    data = entry_adapter.data_merge(json_data)
    return JSONResponse(content=data)
