from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.deps import get_db

router = APIRouter()

@router.post("/")
async def create_offer(db: AsyncSession = Depends(get_db)):
    return {"message": "Create casting offer endpoint"}
