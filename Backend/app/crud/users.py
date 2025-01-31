from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Sequence, Annotated
from fastapi import Form, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
from auth import utils as auth_utils
from auth.utils import hash_password, validate_password
from core.models import User
from sqlalchemy import select
from auth import utils as auth_utils
from core.schemas.user import UserRegister, UserLogin
from core.schemas.user import Token
# from crud.validate_auth import validate_auth_user


#
#
# async def get_all_users(session: AsyncSession) -> Sequence[User]:
#     stmt = select(User).order_by(User.id)
#     result = await session.scalars(stmt)
#     return result.all()
#
# async def create_user(
#         session: AsyncSession,
#         user_create: UserCreate,
# ):
#     user = User(**user_create.model_dump())
#     session.add(user)
#     await session.commit()
#     await session.refresh(user)
#     return user
#
#

async def register_user(
        session: AsyncSession,
        user_reg: UserRegister,
) -> User:
    stmt = select(User).where(User.username == user_reg.username)
    result = await session.execute(stmt)
    existing_user = result.scalar_one_or_none()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Пользователь с таким именем уже существует",
        )
    hashed_password = hash_password(user_reg.password)
    user = User(
        username=user_reg.username,
        password=hashed_password,
    )
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user


async def login_user(
        user_log: UserLogin,
        session: AsyncSession,
        username: str = Form(...),
        password: str = Form(...),
) -> Token:
    stmt = select(User).where(User.username == username)
    result = await session.execute(stmt)
    user = result.scalar_one_or_none()

    if not user or not auth_utils.validate_password(password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )

    # if not user.active:
    #     raise HTTPException(
    #         status_code=status.HTTP_403_FORBIDDEN,
    #         detail="User is inactive"
    #     )
    else:
        jwt_payload = {
            "sub": user_log.username,
            "username": user_log.username,
        }
        token = auth_utils.encoded_jwt(jwt_payload)
        return Token(
            access_token=token,
            token_type="bearer",
        )


