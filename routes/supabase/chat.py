from fastapi import APIRouter
from db.supabase import supabase
from schemas.chat import ChatRequest

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
    respone = (
        supabase.table("chatting")
        .update({
            "chat": req.model_dump()["chats"]
        })
        .eq("user_uuid", user_id)
        .execute()
    )
    print("요청",req)

    return("에러", respone)
