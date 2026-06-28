from schemas.travel_destination.travel_destination import REGION_ALIASES

# 지역명을 정규화 하는 함수
# 매개 변수로 REGION_ALIASES(지역별칭 정규화 맵)의 key(정규화전 지역별칭)값을 입력받음
# REGION_ALIASES(지역별칭 정규화 맵)의 존재하는 지역 별칭이면 정규화된 지역 별칭을 반환 만약 없다면 None을 반환
def normalize_region(raw_region: str) -> str | None:
    # get.(key)형식으로 사용 key값의 맞는 value를 반환함
    return REGION_ALIASES.get(raw_region)

# 사용자의 프롬프트에서 지역명을 찾는 함수
# 매개변수로 사용자의 프롬프트를 입력받음
# 지역 별칭을 찾으면 지역별칭을 반환하고 못찾으면 None을 반환
def extract_region_raw(user_text: str) -> str | None:
    # REGION_ALIASES(지역별칭 정규화 맵)의 key값을 하나씩 alias라는 변수에 담으며 순회함
    for alias in REGION_ALIASES.keys():
        # 사용자 프롬프트 안에 alias(지역별칭)이 존재하면 지역 별칭을 반환
        if alias in user_text:
            return alias
    
    return None

# print(extract_region_raw("친구랑 제주 여행을 가려고 하는데 서귀포 여행지 추천해줘"))
