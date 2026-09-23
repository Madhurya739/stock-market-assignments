import os
from fastapi import APIRouter, Path, HTTPException
from fastapi.responses import FileResponse

router = APIRouter(prefix="/companies", tags=["companies"])

@router.get("/{ticker}/tearsheet")
def get_company_tearsheet(ticker: str = Path(..., description="Company ticker symbol")):
    # Construct file path — adjust directory as needed
    file_path = f"reports/tearsheets/{ticker}_tearsheet.pdf"

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Tearsheet PDF not found")

    return FileResponse(
        path=file_path,
        media_type="application/pdf",
        filename=f"{ticker}_tearsheet.pdf"
    )
