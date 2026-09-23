from fastapi import APIRouter, HTTPException

router = APIRouter()

# Example dataset (reuse your COMPANIES list if already defined elsewhere)
COMPANIES = [
    {
        "company_id": 1,
        "company_name": "Tata Consultancy Services",
        "ticker": "TCS",
        "broad_sector": "IT",
    },
    {
        "company_id": 2,
        "company_name": "Infosys",
        "ticker": "INFY",
        "broad_sector": "IT",
    },
    {
        "company_id": 3,
        "company_name": "Reliance Industries",
        "ticker": "RELIANCE",
        "broad_sector": "Energy",
    },
    {
        "company_id": 4,
        "company_name": "HDFC Bank",
        "ticker": "HDFCBANK",
        "broad_sector": "Financials",
    },
    {
        "company_id": 5,
        "company_name": "ICICI Bank",
        "ticker": "ICICIBANK",
        "broad_sector": "Financials",
    },
    # … continue until you have 92 companies …
]


@router.get("/sectors")
def list_sectors():
    """TODO: Add docstring."""
    sectors = sorted(set(c["broad_sector"] for c in COMPANIES))
    return {"count": len(sectors), "sectors": sectors}


@router.get("/sectors/{sector}")
def get_sector_companies(sector: str):
    """TODO: Add docstring."""
    filtered = [c for c in COMPANIES if c["broad_sector"].upper() == sector.upper()]
    if not filtered:
        raise HTTPException(status_code=404, detail="Sector not found")
    return {"count": len(filtered), "companies": filtered}
