from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from app.db.base import Base

class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=True) # 소셜 로그인만 있는 경우 null 가능
    role_type = Column(String, nullable=True) # actor, agency
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class SocialIdentity(Base):
    __tablename__ = "social_identities"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True, nullable=False)
    provider = Column(String, nullable=False) # kakao, google, apple 등
    provider_subject = Column(String, nullable=False, index=True) # 소셜 측 고유 ID
    created_at = Column(DateTime(timezone=True), server_default=func.now())
