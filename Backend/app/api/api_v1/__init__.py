from fastapi import APIRouter

from api.api_v1 import users
from core import settings
from .users import router as users_router

router = APIRouter(
    prefix=settings.api.v1.users,
)
router.include_router(users_router)