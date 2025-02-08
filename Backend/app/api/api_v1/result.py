from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from utils.access_token import get_current_token_user
from crud.results import create_result, get_user_results
from core import db_helper
from fastapi import Query, Depends, HTTPException
router = APIRouter()

@router.post("/results")
async def save_result(
    result: int = Query(...),
    current_user: dict = Depends(get_current_token_user),
    session: AsyncSession = Depends(db_helper.session_getter)
):
    try:
        user_id = int(current_user["sub"])
        return await create_result(session, result, user_id)
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(
            status_code=400,
            detail="Не удалось сохранить результат"
        )

@router.get("/results")
async def read_results(
    current_user: dict = Depends(get_current_token_user),
    session: AsyncSession = Depends(db_helper.session_getter)
):
    try:
        user_id = current_user.get("sub")
        return await get_user_results(session, user_id)
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail="Не удалось получить результаты"
        )