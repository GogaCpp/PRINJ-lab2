import uuid
from fastapi import HTTPException, status

from chat.schemas.chat import ChatCreatePayload

chat_list = [
    {
        "id": uuid.uuid1(),
        "name": "123123",
        "is_group": "root",
        "creator_id": uuid.uuid1()
    }
]


class ChatService():
    def __init__(self):
        ...

    async def get_chat_by_id(self, id: uuid.UUID):
        for chat in chat_list:
            if chat["id"] == id:
                return chat
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    async def get_chat_list(self):
        return {"chat_list": chat_list}

    async def create_chat(self, chat: ChatCreatePayload, user_id: str):
        new_chat = chat.model_dump(exclude_unset=True)
        new_chat["id"] = uuid.uuid1()
        new_chat["creator_id"] = uuid.UUID(user_id)
        chat_list.append(new_chat)
        return new_chat

    async def delete_chat(self, id: uuid.UUID):
        for chat in chat_list:
            if chat["id"] == id:
                chat_list.remove(chat)

