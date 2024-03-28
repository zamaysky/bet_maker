import uvicorn
from fastapi import FastAPI

from config import settings
from routes.bets import router as bets_router
from routes.events import router as events_router

app = FastAPI(title=settings.APP_TITLE)

app.include_router(bets_router)
app.include_router(events_router)

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host=settings.APP_HOST, port=settings.APP_PORT,
    )
