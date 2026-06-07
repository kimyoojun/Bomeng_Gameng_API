from fastapi import APIRouter
from db.supabase import supabase

router = APIRouter(prefix="/users/{user_id}/chats", tags=["chats"])

@router.get("/")
async def select_chat(user_id: str):
    print("유저 아이디",user_id)
    response = (
        supabase.table("chatting")
        .select("chat")
        .eq("user_uuid", user_id)
        .execute()
    )
    
    return response.data
