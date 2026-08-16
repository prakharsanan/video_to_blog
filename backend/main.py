from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.api.routes import router

app = FastAPI(
    title="Video to Blog API",
    description="Convert YouTube videos into AI-generated blogs with extracted images.",
    version="1.0.0",
)

# Allow frontend (React/Vite) to access the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(router)

# Serve static files (images, blogs, videos, transcripts, etc.)
app.mount(
    "/storage",
    StaticFiles(directory="storage"),
    name="storage",
)


@app.get("/")
def root():
    return {
        "status": "success",
        "message": "🚀 Video to Blog API is running."
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }