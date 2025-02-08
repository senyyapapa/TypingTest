from contextlib import asynccontextmanager
from fastapi.responses import ORJSONResponse
from fastapi import FastAPI
import uvicorn
from api import router as api_router
from core import db_helper
from core import settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    #startup
    yield
    #shutdown
    print('dispose engine')
    await db_helper.dispose()
main_app = FastAPI(
    lifespan=lifespan,
    default_response_class=ORJSONResponse,
)

main_app.include_router(
    api_router,
)


if __name__ == "__main__":
    uvicorn.run(
        'main:main_app',
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )