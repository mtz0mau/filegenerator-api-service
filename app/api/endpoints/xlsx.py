from fastapi import APIRouter, Request, HTTPException
from app.adapters import entry_adapter
from app.repositories.xlsx import generate_xlsx

router = APIRouter()

@router.post("/")
async def create_xlsx(request: Request):
    json_data = await request.json()

    if not isinstance(json_data, list):
        raise HTTPException(status_code=422, detail="JSON data must be a list")

    if not json_data:
        raise HTTPException(status_code=422, detail="JSON data is empty")

    data = entry_adapter.data_merge(json_data)
    file_path = generate_xlsx(data)
    
    return {"file_path": file_path}
