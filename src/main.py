import uvicorn
from fastapi import FastAPI
from routes.bets import router as thematic_router

app = FastAPI(title="ThematicAPI", version="1.0", openapi_url="/openapi.json", docs_url="/docs")

app.include_router(thematic_router)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000, debug=True)
