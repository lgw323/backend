from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from app.api.deps import get_db
from app.crud import crud_profile
from app.schemas.profile import ActorSearchResponse

router = APIRouter()

@router.get("/search/actors", response_model=List[ActorSearchResponse])
async def search_actors_api(
    birth_year: Optional[int] = Query(None, description="생년 (예: 1995)"),
    gender: Optional[str] = Query(None, description="성별 (예: male, female)"),
    region: Optional[str] = Query(None, description="활동 지역 (예: 서울)"),
    min_filmo_count: Optional[int] = Query(0, description="최소 필모 수"),
    max_filmo_count: Optional[int] = Query(None, description="최대 필모 수"),
    db: AsyncSession = Depends(get_db)
):
    """
    배우 검색 API
    """
    actors = await crud_profile.search_actors(
        db=db,
        birth_year=birth_year,
        gender=gender,
        region=region,
        min_filmo_count=min_filmo_count,
        max_filmo_count=max_filmo_count
    )
    return actors

@router.get("/")
async def get_profiles(db: AsyncSession = Depends(get_db)):
    return {"message": "Get profiles"}

@router.get("/{slug}")
async def get_public_portfolio(slug: str, db: AsyncSession = Depends(get_db)):
    return {"message": f"Public portfolio for {slug}"}
