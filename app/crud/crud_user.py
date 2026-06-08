from typing import Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User
from app.models.profile import Profile
from app.schemas.user import UserSignupActor, UserSignupAgency, RoleType
from app.core.security import get_password_hash

async def get_by_email(db: AsyncSession, email: str) -> Optional[User]:
    result = await db.execute(select(User).where(User.email == email))
    return result.scalars().first()

async def get_user_by_id(db: AsyncSession, user_id: int) -> Optional[User]:
    result = await db.execute(select(User).where(User.id == user_id))
    return result.scalars().first()

async def create_actor(db: AsyncSession, obj_in: UserSignupActor) -> User:
    # 1. User 생성
    db_user = User(
        email=obj_in.email,
        hashed_password=get_password_hash(obj_in.password),
        role_type=RoleType.actor.value,
        is_active=True,
    )
    db.add(db_user)
    await db.flush() # DB에 반영하여 id를 발급받음 (commit 전)

    # 2. Profile 생성
    db_profile = Profile(
        user_id=db_user.id,
        name=obj_in.name,
        profile_image_url=obj_in.profile_image_url,
        introduction=obj_in.introduction,
        age_range=obj_in.age_range,
    )
    db.add(db_profile)
    await db.commit()
    await db.refresh(db_user)
    return db_user

async def create_agency(db: AsyncSession, obj_in: UserSignupAgency) -> User:
    # 1. User 생성
    db_user = User(
        email=obj_in.email,
        hashed_password=get_password_hash(obj_in.password),
        role_type=RoleType.agency.value,
        is_active=True,
    )
    db.add(db_user)
    await db.flush() # DB에 반영하여 id를 발급받음

    # 2. Profile 생성 (에이전시는 agency 필드를 name으로도 사용)
    db_profile = Profile(
        user_id=db_user.id,
        name=obj_in.agency, # 필수 필드인 name에 agency를 저장
        agency=obj_in.agency,
        job_title=obj_in.job_title,
        preferred_genres=obj_in.preferred_genres,
    )
    db.add(db_profile)
    await db.commit()
    await db.refresh(db_user)
    return db_user
