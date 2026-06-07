from pydantic import BaseModel
from typing import Literal

class Chat(BaseModel):
    role: Literal["user", "assistant"]
    content: str

class ChatRequest(BaseModel):
    chats: list[Chat]
    