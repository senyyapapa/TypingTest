
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
# from fastapi.params import Form
# from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import defer
from sqlmodel.ext.asyncio.session import AsyncSession
# from starlette import status
from core import settings, db_helper
# from jwt.exceptions import InvalidTokenError
from crud import users as crud_users
from core.schemas.user import UserRegister, UserLogin



# http_bearer = HTTPBearer()





router = APIRouter(tags=['users'])


@router.post("/registration")
async def reg_user(
        user_reg: UserRegister,
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)]
):
    user = await crud_users.register_user(
        session=session,
        user_reg=user_reg,
    )
    return {"message": "User registered"}


@router.post('/login')
async def auth_user(
        user_login: UserLogin,
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)]
):
    return await crud_users.login_user(
        user_log=user_login,
        session=session,
        username=user_login.username,
        password=user_login.password,
    )


# async def get_current_token_user(
#        credentials: HTTPAuthorizationCredentials = Depends(http_bearer),
# ) -> UserSchema:
#     token = credentials.credentials
#     try:
#         payload = auth_utils.decoded_jwt(token=token)
#     except InvalidTokenError as e:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail=f"invalid token error: {e}",
#         )
#     return payload
#
# async def get_current_auth_user(
#         payload: dict = Depends(get_current_token_user),
# ) -> UserSchema:
#     username: str | None = payload.get("sub")
#     if user := user_db.get(username):
#         return user
#     raise HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="token invalid",
#     )
#
#
#
# async def get_current_active_user(
#         user: UserSchema = Depends(get_current_auth_user),
# ) -> UserSchema:
#     if user.active:
#         return user
#     raise HTTPException(
#         status_code=status.HTTP_403_FORBIDDEN,
#         detail="user inactive",
#     )
#
#
# @router.get("/user/me")
# async def auth_user_check_self_info(
#         user: UserSchema = Depends(get_current_active_user),
# ):
#     return {
#         "username": user.username
#          }