from fastapi import APIRouter

from app.api.v1.endpoints import auth, users, profiles, works, projects, offers

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(profiles.router, prefix="/profiles", tags=["profiles"])
api_router.include_router(works.router, prefix="/works", tags=["works"])
api_router.include_router(projects.router, prefix="/projects", tags=["projects"])
api_router.include_router(offers.router, prefix="/offers", tags=["offers"])
