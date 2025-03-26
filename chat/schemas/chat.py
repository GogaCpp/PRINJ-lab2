import uuid
from pydantic import BaseModel, ConfigDict


class Chat(BaseModel):
    id: uuid.UUID
    name: str
    is_group: str
    creator_id: uuid.UUID


class ChatCreatePayload(BaseModel):
    name: str
    is_group: str


class BaseChat(BaseModel):
    model_config = ConfigDict(from_attributes=True, strict=True)

    id: uuid.UUID
    name: str
    is_group: str
    creator_id: uuid.UUID


class BaseChatList(BaseModel):
    model_config = ConfigDict(from_attributes=True, strict=True)

    chat_list: list[BaseChat]
