from sqlalchemy import Column, Integer, String, JSON, DateTime, Boolean
from sqlalchemy.sql import func
from app.db.base import Base

class Profile(Base):
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    profile_image_url = Column(String, nullable=True)
    hero_image_url = Column(String, nullable=True)
    introduction = Column(String, nullable=True)
    contact_email = Column(String, nullable=True)
    sns_links = Column(JSON, nullable=True)
    
    # 분야, 특기, 소속 등
    activity_field = Column(String, nullable=True)
    skills = Column(JSON, nullable=True)
    agency = Column(String, nullable=True)
    
    # 역할별 추가 필드
    birth_year = Column(Integer, nullable=True) # 배우용 (나이대 대신 생년 저장)
    gender = Column(String, nullable=True) # 배우용 (성별)
    region = Column(String, nullable=True) # 배우용 (활동 지역)
    job_title = Column(String, nullable=True) # 에이전시용 (직무)
    preferred_genres = Column(JSON, nullable=True) # 에이전시용 (선호장르)
    
    # 포트폴리오 공개 여부 및 설정
    portfolio_visibility = Column(String, default="public") # public or private
    field_visibility = Column(JSON, nullable=True) # 개별 필드 비공개 설정
    public_slug = Column(String, unique=True, index=True, nullable=True)
    
    # BM / 기능 확장
    is_premium = Column(Boolean, default=False) # 프리미엄 꾸미기/상단 노출 등
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
