from fastapi import APIRouter

router = APIRouter(prefix="/valuation", tags=["valuation"])

@router.get("/")
def valuation_root():
    return {"message": "Valuation module root"}
