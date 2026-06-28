from fastapi import APIRouter
from starlette.responses import JSONResponse as JSON

from client import supabase, openai
from travel_ai import travel_ai
from schemas.chat import Chat
from db.chat.chat import chat_select, chat_update
from db.recommended.attractions import attractions_select
from schemas.travel_destination.regional_normalization import normalize_region, extract_region_raw

router = APIRouter(prefix="/users/{user_id}/chats", tags=["chats"])

# DB에서 chatting 기록을 select하는 코드
@router.get("/")
async def select_chat(user_id: str):
    chatSelectData = chat_select(user_id)
    
    return chatSelectData

# DB에서 chatting 내역을 추가하는 코드
@router.post("/")
async def add_chat(user_id: str, req: Chat):
    try:
        # 사용자 프롬프트에서 지역 별칭을 추출하여 저장
        extractRegion = extract_region_raw(req.content)

        # 추출한 지역별칭을 정규화후 저장
        normalizeRegion = normalize_region(extractRegion)

        print(normalizeRegion)

        # 정규화된 지역별칭으로 관광지 추천받음
        print(attractions_select(normalizeRegion))


        # # 입력받은 질문을 openai api를 사용하여 전달후 답변을 받음
        # aiAnswer = travel_ai(req.content)

        # # 대화 내역을 저장하기위해 이전 대화 내용을 불러옴
        # chatSelectData = chat_select(user_id)

        # # 이전 대화내용을 chatting 변수에 저장
        # chatting = chatSelectData["chat"]

        # # 이전 대화 내용 배열에 사용자의 질문을 추가하여 저장
        # chatting.append(req.model_dump())

        # ## 지금까지의 대화 내용을 DB에 저장 (사용자의 질문이 추가됨)
        # chat_update(user_id, chatting)

        # # 지금까지의 대화 내용에 AI의 답변 내용을 저장
        # chatting.append({
        #     "role": "assistant",
        #     "content": aiAnswer
        # })

        # # 지금까지의 대화 내용을 DB에 저장(ai 답변이 추가됨)
        # chat_update(user_id, chatting)

    except Exception as e:
        print(e)
        return JSON({"msg": "메세지 전송에 실패하였습니다."}, 500)
    else:
        return JSON({"msg": "메세지 전송에 성공하였습니다."}, 200)
