from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from app.db.base import Base

class Work(Base):
    __tablename__ = "works"
    
    id = Column(Integer, primary_key=True, index=True)
    owner_user_id = Column(Integer, index=True, nullable=False) # 등록자
    
    # 메타데이터
    youtube_url = Column(String, nullable=False)
    youtube_video_id = Column(String, index=True, nullable=False)
    title = Column(String, nullable=False)
    thumbnail_url = Column(String, nullable=True)
    channel_name = Column(String, nullable=True)
    duration_iso = Column(String, nullable=True)
    
    # 추가 정보
    genre = Column(String, nullable=True)
    work_type = Column(String, nullable=True) # 영화, 드라마, 웹드라마 등
    production_year = Column(Integer, nullable=True)
    description = Column(String, nullable=True)
    poster_image_url = Column(String, nullable=True) # 공식 포스터 이미지
    
    # 대표작 및 공개 여부
    is_featured = Column(Boolean, default=False)
    visibility = Column(String, default="public") # public, private
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class WorkCredit(Base):
    __tablename__ = "work_credits"
    
    id = Column(Integer, primary_key=True, index=True)
    work_id = Column(Integer, index=True, nullable=False)
    
    role_code = Column(String, nullable=False) # 감독, 작가, 배우, 촬영, 편집 등
    role_weight = Column(String, nullable=True) # 주연, 조연, 단역 등 (배우용)
    character_name = Column(String, nullable=True) # 배역 이름 (배우용)
    display_name = Column(String, nullable=False) # 표시될 이름 (미가입자 대비)
    linked_user_id = Column(Integer, index=True, nullable=True) # 연결된 가입자 ID
    
    invite_status = Column(String, default="none") # none, pending, sent, linked
    
    created_by = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
