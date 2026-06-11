"""Resume Lens FastAPI application."""
from fastapi import FastAPI

from app.api.routes import router

app = FastAPI(title="Resume Lens API")


@app.get("/")
def health():
    return {"status": "ok", "service": "Resume Lens API"}


app.include_router(router, prefix="/api")
