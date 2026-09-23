from fastapi import APIRouter

router = APIRouter(prefix="/documents", tags=["documents"])

@router.get("/")
def documents_root():
    return {"message": "Documents module root"}
