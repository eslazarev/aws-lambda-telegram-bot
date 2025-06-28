from typing import List, Optional
from pydantic import BaseModel, Field


class User(BaseModel):
    id: int
    is_bot: bool
    first_name: str
    last_name: Optional[str] = None
    username: Optional[str] = None
    language_code: Optional[str] = None


class Chat(BaseModel):
    id: int
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    username: Optional[str] = None
    type: str


class MessageEntity(BaseModel):
    offset: int
    length: int
    type: str


class Photo(BaseModel):
    file_id: str
    file_unique_id: str
    file_size: int
    width: int
    height: int


class Document(BaseModel):
    file_id: str
    file_unique_id: str
    file_size: int
    mime_type: str
    file_name: Optional[str] = None


class ChatMemberStatus(BaseModel):
    user: User
    status: str
    until_date: Optional[int] = None


class Message(BaseModel):
    message_id: int
    from_: User = Field(..., alias="from")
    chat: Chat
    date: int
    text: Optional[str] = None
    entities: Optional[List[MessageEntity]] = None
    media_group_id: Optional[str] = None
    photo: Optional[List[Photo]] = None
    document: Optional[Document] = None


class MyChatMember(BaseModel):
    chat: Chat
    from_: User = Field(..., alias="from")
    date: int
    old_chat_member: ChatMemberStatus
    new_chat_member: ChatMemberStatus


class TelegramRequest(BaseModel):
    update_id: int
    message: Optional[Message] = None
    my_chat_member: Optional[MyChatMember] = None

    class Config:
        populate_by_name = True
