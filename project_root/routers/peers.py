from fastapi import APIRouter

router = APIRouter(prefix="/peers", tags=["peers"])

@router.get("/")
def peers_root():
    return {"message": "Peers module root"}
