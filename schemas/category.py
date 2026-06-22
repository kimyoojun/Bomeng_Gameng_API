from pydantic import BaseModel, Field
from typing import Optional, List, Literal

class TravelQuery(BaseModel):
    # 여행지 (부산, 제주, 서울 등)
    region: Optional[str] = Field(default=None, description="여행 지역 또는 도시")

    # 누구랑? 무조건 리스트 안의 값중 하나가 들어가야 함
    #companion: List[Literal["solo", "couple", "friends", "family", "parents"]] = Field(default_factory=list)

    companion: Optional[Literal["solo", "couple", "friends", "family", "parents"]] = Field(default=None, description="여행 동반자")


