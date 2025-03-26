import uuid
from fastapi import HTTPException, status

from ..schemas.user import UserCreatePayload, UserUpdatePayload

user_list = [
    {
        "id": uuid.uuid1(),
        "name": "admin",
        "password": "secret",
        "user_type_id": 3
    }
]


class UserService():
    def __init__(self):
        ...

    async def get_user_by_id(self, id: uuid.UUID):
        for user in user_list:
            if user["id"] == id:
                return user
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    async def get_user_list(self):
        return {"user_list": user_list}

    async def create_user(self, user: UserCreatePayload):
        new_user = user.model_dump(exclude_unset=True)
        new_user["id"] = uuid.uuid1()
        user_list.append(new_user)
        return new_user

    async def update_user(self, id: uuid.UUID, user_base: UserUpdatePayload):
        user = await self.get_user_by_id(id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        update_data = user_base.model_dump(exclude_unset=True)
        # ! мб тут надо по дргом
        for user in user_list:
            if user["id"] == id:
                for key in user:
                    user[key] = update_data.get(key, user[key])

        return user

    async def delete_user(self, id: uuid.UUID):
        for user in user_list:
            if user["id"] == id:
                user_list.remove(user)

    async def auth_user(self, name: str, password: str):
        for user in user_list:
            if user["name"] == name and user["password"] == password:
                return user
        return None
