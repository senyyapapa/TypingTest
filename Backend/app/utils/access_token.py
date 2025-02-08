from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jwt import InvalidTokenError
from core.schemas.user import UserSchema

from auth import utils as auth_utils
http_bearer = HTTPBearer()




async def get_current_token_user(
       credentials: HTTPAuthorizationCredentials = Depends(http_bearer),
) -> UserSchema:
    token = credentials.credentials
    try:
        payload = auth_utils.decoded_jwt(token=token)
        payload['sub'] = int(payload['sub'])
    except InvalidTokenError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"invalid token error: {e}",
        )
    return payload