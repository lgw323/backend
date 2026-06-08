from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.deps import get_db

router = APIRouter()

@router.post("/")
async def create_work_from_url(url: str, db: AsyncSession = Depends(get_db)):
    return {"message": f"Create work from URL: {url}"}

@router.get("/{work_id}")
async def get_work(work_id: int, db: AsyncSession = Depends(get_db)):
    return {"message": f"Get work details for {work_id}"}
