import time
import httpx
import pytest

BASE_URL = "http://127.0.0.1:8000"

TICKERS = ["INFY", "HDFCBANK", "HINDUNILVR", "RELIANCE", "SUNPHARMA"]


@pytest.mark.parametrize("ticker", TICKERS)
def test_company_profile_load_time(ticker):
    start = time.time()

    with httpx.Client(base_url=BASE_URL) as client:
        response = client.get(f"/companies/{ticker}")
        response.raise_for_status()
        data = response.json()

    elapsed = time.time() - start
    assert elapsed < 3, f"Profile load for {ticker} took {elapsed:.2f}s"

    # Optional: validate structure
    assert "company_name" in data
    assert "ticker" in data
