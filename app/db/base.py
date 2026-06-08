from typing import Any
from sqlalchemy.ext.declarative import as_declarative, declared_attr

@as_declarative()
class Base:
    id: Any
    __name__: str
    
    # 자동으로 테이블 이름을 클래스 이름의 소문자로 설정
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
