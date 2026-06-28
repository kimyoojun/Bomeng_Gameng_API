# 여행지 추천기능 중 에서 DB에 저장하거나 DB에서 불러오는 코드를 작성

from client import supabase

# 입력받은 지역의 관광지를 추천하는 함수
def attractions_select(region: str):
    select = (
        supabase
        .table("jeju_tourist")
        .select("관광지명")
        .or_(f"소재지도로명주소.ilike.%{region}%,소재지지번주소.ilike.%{region}%")
        .execute()
    )

    return select.data
