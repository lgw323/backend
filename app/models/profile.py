from sqlalchemy import Column, Integer, String, JSON, DateTime
from sqlalchemy.sql import func
from app.db.base import Base

class Profile(Base):
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    profile_image_url = Column(String, nullable=True)
    introduction = Column(String, nullable=True)
    contact_email = Column(String, nullable=True)
    sns_links = Column(JSON, nullable=True)
    
    # 분야, 특기, 소속 등
    activity_field = Column(String, nullable=True)
    skills = Column(JSON, nullable=True)
    agency = Column(String, nullable=True)
    
    # 포트폴리오 공개 여부
    portfolio_visibility = Column(String, default="public") # public or private
    public_slug = Column(String, unique=True, index=True, nullable=True)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
