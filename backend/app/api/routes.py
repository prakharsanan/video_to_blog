from fastapi import APIRouter
from pydantic import BaseModel

from app.services.pipeline_service import PipelineService

router = APIRouter()


class VideoRequest(BaseModel):
    url: str


@router.get("/")
def home():
    return {
        "status": "success",
        "message": "Video to Blog API is running 🚀"
    }


@router.get("/health")
def health():
    return {
        "status": "healthy"
    }


@router.post("/generate")
def generate_blog(request: VideoRequest):

    result = PipelineService.run(request.url)

    return {
        "status": "success",
        **result
    }