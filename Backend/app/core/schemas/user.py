from typing import Annotated

from pydantic import BaseModel, ConfigDict



class UserBase(BaseModel):
    id: int
    username: str
    password: str
    active: bool = True

class Token(BaseModel):
    access_token: str
    token_type: str

class UserSchema(BaseModel):
    id: int
    username: str

class UserRegister(UserBase):
    model_config = ConfigDict(strict=True)

class UserLogin(UserBase):
    model_config = ConfigDict(strict=True)