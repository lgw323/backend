from datetime import timedelta
from typing import Any
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from app.api import deps
from app.core import security
from app.core.config import settings
from app.crud import crud_user
from app.schemas.user import UserSignupActor, UserSignupAgency, UserResponse
from app.schemas.token import Token

router = APIRouter()

@router.post("/signup/actor", response_model=UserResponse)
async def signup_actor(
    *,
    db: AsyncSession = Depends(deps.get_db),
    user_in: UserSignupActor,
) -> Any:
    """
    배우 회원가입
    """
    if user_in.password != user_in.password_confirm:
        raise HTTPException(status_code=400, detail="Passwords do not match")
        
    user = await crud_user.get_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists in the system.",
        )
    user = await crud_user.create_actor(db, obj_in=user_in)
    return user

@router.post("/signup/agency", response_model=UserResponse)
async def signup_agency(
    *,
    db: AsyncSession = Depends(deps.get_db),
    user_in: UserSignupAgency,
) -> Any:
    """
    에이전시 회원가입
    """
    if user_in.password != user_in.password_confirm:
        raise HTTPException(status_code=400, detail="Passwords do not match")
        
    user = await crud_user.get_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists in the system.",
        )
    user = await crud_user.create_agency(db, obj_in=user_in)
    return user

@router.post("/login", response_model=Token)
async def login_access_token(
    db: AsyncSession = Depends(deps.get_db),
    form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    """
    이메일과 비밀번호로 JWT Access Token 발급
    """
    user = await crud_user.get_by_email(db, email=form_data.username)
    if not user or not security.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password",
        )
    elif not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Inactive user",
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": security.create_access_token(
            user.id, expires_delta=access_token_expires
        ),
        "token_type": "bearer",
    }
