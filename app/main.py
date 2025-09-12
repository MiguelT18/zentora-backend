import os
import uvicorn
from fastapi import FastAPI
from app.api.v1.routes import router as api_v1_router

app = FastAPI(title="Zentora API", version="0.1.0")

app.include_router(api_v1_router, prefix="/api/v1")

if __name__ == "__main__":
  uvicorn.run(
    "app.main:app",
    host="0.0.0.0",
    port=8000,
    reload=True if os.getenv("DEBUG") == True else False
  )