import pytest
import pandas as pd
from pathlib import Path

DATA_DIR = Path("C:/Users/srisa/Desktop/Week_2 Stock Market/project_root")

EXPECTED_SCHEMAS = {
    "companies.csv": ["company_id", "company_name", "ticker"],
    "prices.csv": ["company_id", "date_id", "price"],
    "pl.csv": ["company_id", "date_id", "revenue", "expenses", "net_income"],
    "bs.csv": ["company_id", "date_id", "assets", "liabilities", "equity"],
    "cf.csv": ["company_id", "date_id", "cash_in", "cash_out"],
}

EXPECTED_ROW_COUNTS = {
    "companies.csv": 3,
    "prices.csv": 3,
    "pl.csv": 3,
    "bs.csv": 3,
    "cf.csv": 3,
}


@pytest.mark.parametrize("filename", list(EXPECTED_SCHEMAS.keys()))
def test_columns_match(filename):
    df = pd.read_csv(DATA_DIR / filename)
    expected_cols = EXPECTED_SCHEMAS[filename]
    assert list(df.columns) == expected_cols, f"{filename} columns mismatch"


@pytest.mark.parametrize("filename", list(EXPECTED_ROW_COUNTS.keys()))
def test_row_counts(filename):
    df = pd.read_csv(DATA_DIR / filename)
    expected_count = EXPECTED_ROW_COUNTS[filename]
    assert len(df) == expected_count, f"{filename} row count mismatch"
