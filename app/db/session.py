from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

# 엔진 생성
engine = create_async_engine(
    settings.SQLALCHEMY_DATABASE_URI,
    echo=False,  # 개발 중 SQL 쿼리 로깅을 원하면 True로 설정
    future=True,
)

# 세션 팩토리
AsyncSessionLocal = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False, autocommit=False, autoflush=False
)

# 의존성 주입용 제너레이터
async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session
