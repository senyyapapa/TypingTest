from typing import Annotated

from pydantic import BaseModel, ConfigDict



class UserBase(BaseModel):
    username: str
    password: str
    active: bool = True

class Token(BaseModel):
    access_token: str
    token_type: str

class UserRegister(UserBase):
    model_config = ConfigDict(strict=True)

class UserLogin(UserBase):
    model_config = ConfigDict(strict=True)