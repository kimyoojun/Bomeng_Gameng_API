from fastapi import APIRouter
from db.supabase import supabase
from schemas.chat import ChatRequest
from starlette.responses import JSONResponse as JSON

router = APIRouter(prefix="/users/{user_id}/chats", tags=["chats"])

@router.get("/")
async def select_chat(user_id: str):
    response = (
        supabase.table("chatting")
        .select("chat")
        .eq("user_uuid", user_id)
        .execute()
    )
    
    return response.data
    
@router.post("/")
async def add_chat(user_id: str, req: ChatRequest):
    try:
        response = (
            supabase.table("chatting")
            .update({
                "chat": req.model_dump()["chats"]
            })
            .eq("user_uuid", user_id)
            .execute()
        )
    except response.error:
        return JSON({"msg": "메세지 전송에 실패하였습니다."}, 500)
    else:
        return JSON({"msg": "메세지전송에 성공하였습니다"}, 200)

    

