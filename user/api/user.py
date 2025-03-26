import uuid
from fastapi import APIRouter, Depends, status

from user.services.user import UserService
from user.schemas.user import BaseUser, BaseUserList, UserCreatePayload, UserUpdatePayload
from user.config import oauth2_scheme

router = APIRouter(prefix="/user")


@router.get("/", response_model=BaseUserList)
async def get_list(
    token: str = Depends(oauth2_scheme),

    user_service: UserService = Depends()
):
    return await user_service.get_user_list()


@router.get("/{user_id}", response_model=BaseUser)
async def get_user(
    user_id: uuid.UUID,
    token: str = Depends(oauth2_scheme),

    user_service: UserService = Depends()
):
    return await user_service.get_user_by_id(user_id)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=BaseUser)
async def create_user(
    user: UserCreatePayload,
    user_service: UserService = Depends(),
):
    return await user_service.create_user(user)


@router.patch("/{user_id}", response_model=BaseUser)
async def update_user(
    user_id: uuid.UUID,
    user: UserUpdatePayload,
    token: str = Depends(oauth2_scheme),
    user_service: UserService = Depends()
):
    return await user_service.update_user(user_id, user)


@router.delete("/{user_id}")
async def delete_user(
    user_id: uuid.UUID,
    token: str = Depends(oauth2_scheme),
    user_service: UserService = Depends()
):
    return await user_service.delete_user(user_id)