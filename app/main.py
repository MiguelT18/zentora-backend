import os
import uvicorn
from fastapi import FastAPI
from api.v1.routes import router as api_v1_router

app = FastAPI(title="Zentora API", version="0.1.0")

app.include_router(api_v1_router, prefix="/api/v1")

@app.get("/")
async def health_check():
  return {"status": "ok"}

if __name__ == "__main__":
  uvicorn.run(
    "__main__:app",
    host="0.0.0.0",
    port=int(os.getenv("PORT", 8000)),
    reload=True if os.getenv("DEBUG") == True else False
  )