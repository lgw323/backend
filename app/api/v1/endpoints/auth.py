from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.deps import get_db

router = APIRouter()

@router.post("/signup")
async def signup(db: AsyncSession = Depends(get_db)):
    return {"message": "Signup endpoint"}

@router.post("/login")
async def login(db: AsyncSession = Depends(get_db)):
    return {"message": "Login endpoint"}
