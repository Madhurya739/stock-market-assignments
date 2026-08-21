import pandas as pd

def load_excel(path: str) -> pd.DataFrame:
    """Load Excel file into DataFrame."""
    return pd.read_excel(path)

def normalize_year(year_value) -> int:
    """
    Normalize year values:
    - Accepts int, float, str (e.g., '2020', '2020.0')
    - Returns int year
    - Raises ValueError if invalid
    """
    try:
        year = int(float(year_value))
        if 1900 <= year <= 2100:
            return year
        raise ValueError(f"Year out of range: {year}")
    except Exception as e:
        raise ValueError(f"Invalid year: {year_value}") from e

def normalize_ticker(ticker: str) -> str:
    """
    Normalize stock tickers:
    - Strip whitespace
    - Uppercase
    - Remove special characters except '.' and '-'
    """
    if not isinstance(ticker, str):
        raise ValueError("Ticker must be a string")
    clean = ticker.strip().upper()
    return "".join(ch for ch in clean if ch.isalnum() or ch in ['.', '-'])
