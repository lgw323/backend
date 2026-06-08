from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.deps import get_db

router = APIRouter()

@router.get("/")
async def get_profiles(db: AsyncSession = Depends(get_db)):
    return {"message": "Get profiles"}

@router.get("/{slug}")
async def get_public_portfolio(slug: str, db: AsyncSession = Depends(get_db)):
    return {"message": f"Public portfolio for {slug}"}
