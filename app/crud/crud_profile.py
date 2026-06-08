from typing import Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from app.models.profile import Profile
from app.models.user import User
from app.models.work import WorkCredit
from app.schemas.profile import ActorSearchResponse

async def search_actors(
    db: AsyncSession,
    birth_year: Optional[int] = None,
    gender: Optional[str] = None,
    region: Optional[str] = None,
    min_filmo_count: Optional[int] = None,
    max_filmo_count: Optional[int] = None
) -> List[ActorSearchResponse]:
    # 서브쿼리로 해당 유저의 필모 수 계산 (linked_user_id 기준)
    filmo_subq = (
        select(func.count(WorkCredit.id))
        .where(WorkCredit.linked_user_id == Profile.user_id)
        .scalar_subquery()
    )

    query = (
        select(Profile, filmo_subq.label("filmo_count"))
        .join(User, User.id == Profile.user_id)
        .where(User.role_type == "actor")
        .where(Profile.portfolio_visibility == "public")
    )

    if birth_year:
        query = query.where(Profile.birth_year == birth_year)
    if gender:
        query = query.where(Profile.gender == gender)
    if region:
        query = query.where(Profile.region == region)

    if min_filmo_count is not None:
        query = query.where(filmo_subq >= min_filmo_count)
    if max_filmo_count is not None:
        query = query.where(filmo_subq <= max_filmo_count)

    result = await db.execute(query)
    
    # Profile 객체와 filmo_count 스칼라 값을 가져옴
    rows = result.all()
    
    response_list = []
    for profile_obj, filmo_count in rows:
        response_list.append(
            ActorSearchResponse(
                user_id=profile_obj.user_id,
                name=profile_obj.name,
                profile_image_url=profile_obj.profile_image_url,
                introduction=profile_obj.introduction,
                birth_year=profile_obj.birth_year,
                gender=profile_obj.gender,
                region=profile_obj.region,
                filmo_count=filmo_count
            )
        )
        
    return response_list
