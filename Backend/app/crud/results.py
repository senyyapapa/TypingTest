from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Result


async def create_result(
        session: AsyncSession,
        result: int,
        user_id: int
):
    new_result = Result(
        user_id=user_id,
        result=result
    )
    session.add(new_result)
    await session.commit()
    await session.refresh(new_result)
    return new_result


async def get_user_results(
        session: AsyncSession,
        user_id: str
):
    stmt = select(Result).where(Result.user_id == user_id)
    results = await session.execute(stmt)
    results_list = results.scalars().all()

    return {
        "results": [
            {
                "id": result.id,
                "result": result.result,
                "user_id": result.user_id
            } for result in results_list
        ]
    }