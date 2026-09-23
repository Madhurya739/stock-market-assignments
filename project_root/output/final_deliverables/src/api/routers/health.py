# src/api/routers/health.py
from fastapi import APIRouter
import time

router = APIRouter()
START_TIME = time.time()

TABLES = [
    "companies",
    "sectors",
    "peers",
    "valuation",
    "portfolio",
    "documents",
    "screener",
    "transactions",
    "users",
    "logs",
]


@router.get("/health/")
def health_check():
    """TODO: Add docstring."""
    uptime_seconds = int(time.time() - START_TIME)
    db_row_counts = {table: 0 for table in TABLES}  # stub counts

    return {
        "status": "ok",
        "db_row_counts": db_row_counts,
        "uptime_seconds": uptime_seconds,
        "version": "1.0.0",
    }
