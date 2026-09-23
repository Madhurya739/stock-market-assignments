from fastapi import APIRouter

router = APIRouter(prefix="/sectors", tags=["sectors"])

@router.get("/")
def sectors_root():
    return {"message": "Sectors module root"}
