from fastapi import APIRouter

router = APIRouter()


@router.get("/screener")
def screener(sector: str, min_roe: int, pe_ratio: float = None):
    """Return filtered screener results based on sector and financial metrics."""
    ...


@router.get("/companies/{ticker}")
def company_profile(ticker: str):
    """Return company profile data for the given ticker."""
    ...


@router.get("/kpis")
def kpis(company_id: str, year: int):
    """Return financial KPIs for a company in a given year."""
    ...
