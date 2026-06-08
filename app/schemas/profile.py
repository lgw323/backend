from pydantic import BaseModel
from typing import Optional, List, Dict, Any

# ==========================================
# 기존 검색용 스키마 업데이트
# ==========================================
class ActorSearchResponse(BaseModel):
    user_id: int
    name: str
    profile_image_url: Optional[str] = None
    introduction: Optional[str] = None
    birth_year: Optional[int] = None
    gender: Optional[str] = None
    region: Optional[str] = None
    filmo_count: int = 0

    class Config:
        from_attributes = True


# ==========================================
# 마이페이지 수정용 스키마
# ==========================================
class ProfileUpdate(BaseModel):
    name: Optional[str] = None
    profile_image_url: Optional[str] = None
    hero_image_url: Optional[str] = None
    introduction: Optional[str] = None
    contact_email: Optional[str] = None
    sns_links: Optional[Dict[str, str]] = None
    
    activity_field: Optional[str] = None
    skills: Optional[List[str]] = None
    agency: Optional[str] = None
    
    birth_year: Optional[int] = None
    gender: Optional[str] = None
    region: Optional[str] = None
    
    portfolio_visibility: Optional[str] = None
    field_visibility: Optional[Dict[str, str]] = None


# ==========================================
# 배우 마이페이지(포트폴리오) 응답 스키마
# ==========================================

class FeaturedVideo(BaseModel):
    work_id: int
    youtube_url: str
    title: str
    thumbnail_url: Optional[str] = None

class FilmographyWork(BaseModel):
    work_id: int
    work_type: Optional[str] = None # MOVIE, DRAMA 등
    title: str
    poster_image_url: Optional[str] = None
    role_weight: Optional[str] = None # LEAD, SUPPORT 등
    character_name: Optional[str] = None

class FilmographyYearGroup(BaseModel):
    year: int
    works: List[FilmographyWork]

class ProfileBasicInfo(BaseModel):
    name: str
    birth_year: Optional[int] = None
    profile_image_url: Optional[str] = None
    hero_image_url: Optional[str] = None
    introduction: Optional[str] = None
    filmo_count: int = 0
    is_premium: bool = False

class ActorMyPageResponse(BaseModel):
    profile: ProfileBasicInfo
    skills: List[str] = []
    featured_videos: List[FeaturedVideo] = []
    filmographies: List[FilmographyYearGroup] = []
