import os
import zipfile
import tempfile
from fastapi import APIRouter, Query, HTTPException
from fastapi.responses import FileResponse

router = APIRouter(prefix="/portfolio", tags=["portfolio"])

@router.get("/tearsheets")
def get_portfolio_tearsheets(
    tickers: list[str] = Query(..., description="List of company tickers to include")
):
    # Directory where tearsheets are stored
    base_dir = "reports/tearsheets"

    # Collect file paths
    file_paths = []
    for ticker in tickers:
        path = os.path.join(base_dir, f"{ticker}_tearsheet.pdf")
        if not os.path.exists(path):
            raise HTTPException(status_code=404, detail=f"Tearsheet not found for {ticker}")
        file_paths.append(path)

    # Create temporary ZIP file
    tmp_zip = tempfile.NamedTemporaryFile(delete=False, suffix=".zip")
    with zipfile.ZipFile(tmp_zip.name, "w") as zipf:
        for file_path in file_paths:
            zipf.write(file_path, arcname=os.path.basename(file_path))

    return FileResponse(
        path=tmp_zip.name,
        media_type="application/zip",
        filename="portfolio_tearsheets.zip"
    )
