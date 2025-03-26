from fastapi.security import OAuth2PasswordBearer
from datetime import timedelta
from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    model_config = ConfigDict(extra='ignore')

    algorithm: str
    secret_key: str

    @property
    def access_token_expire(self):
        return timedelta(minutes=self.ACCESS_TOKEN_EXPIRE_MINUTES)


settings = Settings(
    _env_file=".env",
    _env_file_encoding="utf-8"
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")
