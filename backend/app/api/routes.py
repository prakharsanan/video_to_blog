from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def root():
    return {
        "status": "success",
        "message": "Video to Blog API is running 🚀"
    }

@router.get("/health")
def health():
    return {
        "status": "healthy"
    }