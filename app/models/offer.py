from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.db.base import Base

class Offer(Base):
    __tablename__ = "offers"
    
    id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(Integer, index=True, nullable=False) # 제안 보낸 감독/제작자
    receiver_id = Column(Integer, index=True, nullable=False) # 제안 받은 배우
    project_id = Column(Integer, index=True, nullable=False)
    character_id = Column(Integer, index=True, nullable=False)
    
    message = Column(String, nullable=True)
    reference_links = Column(String, nullable=True)
    response_deadline = Column(DateTime(timezone=True), nullable=True)
    request_audition = Column(String, nullable=True) # 오디션 요청 여부 플래그/설명
    
    status = Column(String, default="pending") # pending, accepted, rejected, audition_submitted, closed
    rejection_reason = Column(String, nullable=True)
    audition_link = Column(String, nullable=True)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
