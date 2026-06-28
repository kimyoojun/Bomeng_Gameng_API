from fastapi import APIRouter
from starlette.responses import JSONResponse as JSON

from client import supabase, openai
from travel_ai import travel_ai
from schemas.chat import Chat

router = APIRouter(prefix="/users/{user_id}/chats", tags=["chats"])

# DB에서 chatting 기록을 select하는 코드
@router.get("/")
async def select_chat(user_id: str):
    response = (
        supabase.table("chatting")
        .select("chat")
        .eq("user_uuid", user_id)
        .single()
        .execute()
    )
    
    return response.data

# DB에서 chatting 내역을 추가하는 코드
@router.post("/")
async def add_chat(user_id: str, req: Chat):
    try:
        # 입력받은 질문을 openai api를 사용하여 전달후 답변을 받음
        aiAnswer = travel_ai(req.content)

        # 대화 내역을 저장하기위해 이전 대화 내용을 불러옴
        select = (
            supabase.table("chatting")
            .select("chat")
            .eq("user_uuid", user_id)
            .single()
            .execute()
        )

        # 이전 대화내용을 chatting 변수에 저장
        chatting = select.data["chat"]

        # 이전 대화 내용 배열에 사용자의 질문을 추가하여 저장
        chatting.append(req.model_dump())

        ## 지금까지의 대화 내용을 DB에 저장 (사용자의 질문이 추가됨)
        userResponse = (
            supabase.table("chatting")
            .update({
                "chat": chatting
            })
            .eq("user_uuid", user_id)
            .execute()
        )

        # 지금까지의 대화 내용에 AI의 답변 내용을 저장
        chatting.append({
            "role": "assistant",
            "content": aiAnswer
        })

        # 지금까지의 대화 내용을 DB에 저장(ai 답변이 추가됨)
        aiResponse = (
            supabase.table("chatting")
            .update({
                "chat": chatting
            })
            .eq("user_uuid", user_id)
            .execute()
        )

    except Exception as e:
        print(e)
        return JSON({"msg": "메세지 전송에 실패하였습니다."}, 500)
    else:
        return JSON({"msg": "메세지 전송에 성공하였습니다.",
                     "data": chatting }, 200)
