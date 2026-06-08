from datetime import datetime
from typing import Optional, List
from enum import Enum
from pydantic import BaseModel, EmailStr, Field

class RoleType(str, Enum):
    actor = "actor"
    agency = "agency"

# 공통 속성
class UserBase(BaseModel):
    email: EmailStr
    is_active: Optional[bool] = True

# 응답용 스키마
class UserResponse(UserBase):
    id: int
    role_type: RoleType
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

# 회원가입(공통) 요청 파라미터 기반 베이스
class SignupCommon(UserBase):
    password: str = Field(min_length=8, max_length=128)
    password_confirm: str = Field(min_length=8, max_length=128)
    agreed_to_terms: bool = True

# 배우 회원가입 폼
class UserSignupActor(SignupCommon):
    name: str
    profile_image_url: Optional[str] = None
    introduction: Optional[str] = None
    age_range: Optional[str] = None

# 에이전시 회원가입 폼 (회사명/프리랜서 이름을 agency로 받음)
class UserSignupAgency(SignupCommon):
    agency: str
    job_title: Optional[str] = None
    preferred_genres: Optional[List[str]] = None
