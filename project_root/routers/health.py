import time
import sqlite3
from fastapi import APIRouter

router = APIRouter(prefix="/health", tags=["health"])

# Track app start time
START_TIME = time.time()

# List of tables to check
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
    "logs"
]

@router.get("/")
def health_check():
    uptime_seconds = int(time.time() - START_TIME)
    db_row_counts = {}

    try:
        conn = sqlite3.connect("bluestock_mf.db")  # adjust path if needed
        cursor = conn.cursor()
        for table in TABLES:
            try:
                cursor.execute(f"SELECT COUNT(*) FROM {table}")
                count = cursor.fetchone()[0]
                db_row_counts[table] = count
            except Exception:
                db_row_counts[table] = None  # table missing or error
        conn.close()
    except Exception:
        db_row_counts = {table: None for table in TABLES}

    return {
        "status": "ok",
        "db_row_counts": db_row_counts,
        "uptime_seconds": uptime_seconds,
        "version": "1.0.0"
    }
