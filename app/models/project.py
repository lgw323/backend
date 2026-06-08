from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.db.base import Base

class Project(Base):
    __tablename__ = "projects"
    
    id = Column(Integer, primary_key=True, index=True)
    owner_user_id = Column(Integer, index=True, nullable=False) # 감독/제작자
    
    title = Column(String, nullable=False)
    project_type = Column(String, nullable=False) # 영화, 웹드라마 등
    genre = Column(String, nullable=True)
    production_schedule = Column(String, nullable=True)
    synopsis = Column(String, nullable=True)
    status = Column(String, default="recruiting") # recruiting, closed
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class Character(Base):
    __tablename__ = "characters"
    
    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, index=True, nullable=False)
    
    name = Column(String, nullable=False)
    age_range = Column(String, nullable=True)
    gender = Column(String, nullable=True)
    appearance_keywords = Column(String, nullable=True)
    personality = Column(String, nullable=True)
    story = Column(String, nullable=True)
    special_skills = Column(String, nullable=True)
    status = Column(String, default="recruiting")
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
