# 채팅기능중에서 DB에 저장하거나 DB에서 불러오는 코드를 작성
from starlette.responses import JSONResponse as JSON

from client import supabase

# 이전 채팅 기록을 불러오는 코드
# 유저의 uuid를 매개변수로 받음
def chat_select(user_id: str):
    try:
        select = (
            supabase
            .table("chatting")
            .select("chat")
            .eq("user_uuid", user_id)
            .single()
            .execute()
        )

    # 오류 처리 코드
    except Exception as e:
        print("오류가 발생했습니다.", e)
        return None
    # 정상 작동시 실행 코드
    else:
        return select.data
    
# 채팅기록을 업데이트 하는 코드
# 유저 uuid와 업데이트 할 채팅 기록을 매게 변수로 받음
def chat_update(user_id:str, chatting):
    try:
        update = (
            supabase
            .table("chatting")
            .update({
                "chat": chatting
            })
            .eq("user_uuid", user_id)
            .execute()
        )

    # 오류 처리 코드
    except Exception as e:
        print("오류가 발생했습니다.", e)
        return None
    # 정상 작동시 실행 코드
    else:
        print("업데이트 성공")
        return None
