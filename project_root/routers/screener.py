import sqlite3
from fastapi import APIRouter, Query, HTTPException

router = APIRouter(prefix="/screener", tags=["screener"])

@router.get("/")
def screener(
    min_roe: float | None = Query(None, ge=0, le=100, description="Minimum ROE %"),
    max_de: float | None = Query(None, ge=0, description="Maximum Debt/Equity ratio"),
    min_fcf: float | None = Query(None, ge=0, description="Minimum Free Cash Flow"),
    sector: str | None = Query(None, description="Filter by sector"),
    min_rev_cagr_5yr: float | None = Query(None, ge=0, description="Minimum 5yr Revenue CAGR %"),
    min_pat_cagr_5yr: float | None = Query(None, ge=0, description="Minimum 5yr PAT CAGR %"),
    max_pe: float | None = Query(None, ge=0, description="Maximum PE ratio"),
):
    conn = sqlite3.connect("bluestock_mf.db")
    cursor = conn.cursor()

    query = """
        SELECT id, company_name, ticker, broad_sector, roe_pct, de_ratio, fcf,
               rev_cagr_5yr, pat_cagr_5yr, pe_ratio, composite_quality_score
        FROM companies
    """
    conditions, params = [], []

    if min_roe is not None:
        conditions.append("roe_pct >= ?")
        params.append(min_roe)
    if max_de is not None:
        conditions.append("de_ratio <= ?")
        params.append(max_de)
    if min_fcf is not None:
        conditions.append("fcf >= ?")
        params.append(min_fcf)
    if sector:
        conditions.append("broad_sector = ?")
        params.append(sector)
    if min_rev_cagr_5yr is not None:
        conditions.append("rev_cagr_5yr >= ?")
        params.append(min_rev_cagr_5yr)
    if min_pat_cagr_5yr is not None:
        conditions.append("pat_cagr_5yr >= ?")
        params.append(min_pat_cagr_5yr)
    if max_pe is not None:
        conditions.append("pe_ratio <= ?")
        params.append(max_pe)

    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    query += " ORDER BY composite_quality_score DESC"

    try:
        cursor.execute(query, params)
        rows = cursor.fetchall()
    except Exception as e:
        conn.close()
        raise HTTPException(status_code=400, detail=f"Invalid parameter values: {str(e)}")

    conn.close()

    companies = [
        {
            "id": row[0],
            "company_name": row[1],
            "ticker": row[2],
            "broad_sector": row[3],
            "roe_pct": row[4],
            "de_ratio": row[5],
            "fcf": row[6],
            "rev_cagr_5yr": row[7],
            "pat_cagr_5yr": row[8],
            "pe_ratio": row[9],
            "composite_quality_score": row[10],
        }
        for row in rows
    ]

    return {"count": len(companies), "companies": companies}
