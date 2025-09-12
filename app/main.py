from fastapi import FastAPI
from app.api.v1.routes import router as api_v1_router

app = FastAPI(title="Zentora API", version="0.1.0")

app.include_router(api_v1_router, prefix="/api/v1")