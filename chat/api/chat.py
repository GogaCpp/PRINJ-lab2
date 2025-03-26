import uuid
from fastapi import APIRouter, Depends, status

from chat.services.chat import ChatService
from chat.schemas.chat import BaseChat, BaseChatList, ChatCreatePayload
from chat.config import oauth2_scheme
from chat.services.jwt import decode_token

router = APIRouter(prefix="/chat")


@router.get("/", response_model=BaseChatList)
async def get_list(
    token: str = Depends(oauth2_scheme),
    chat_service: ChatService = Depends()
):
    return await chat_service.get_chat_list()


@router.get("/{chat_id}", response_model=BaseChat)
async def get_chat(
    chat_id: uuid.UUID,
    token: str = Depends(oauth2_scheme),
    chat_service: ChatService = Depends()
):
    return await chat_service.get_chat_by_id(chat_id)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=BaseChat)
async def create_chat(
    chat: ChatCreatePayload,
    token: str = Depends(oauth2_scheme),
    chat_service: ChatService = Depends(),
):
    d_tokens = await decode_token(token)
    creator_id = d_tokens["user_id"]
    return await chat_service.create_chat(chat, user_id=creator_id)


@router.delete("/{chat_id}")
async def delete_chat(
    chat_id: uuid.UUID,
    token: str = Depends(oauth2_scheme),
    chat_service: ChatService = Depends()
):
    return await chat_service.delete_chat(chat_id)