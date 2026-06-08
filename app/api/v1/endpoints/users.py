from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.deps import get_db

router = APIRouter()

@router.get("/me")
async def read_users_me(db: AsyncSession = Depends(get_db)):
    return {"message": "My info endpoint"}
