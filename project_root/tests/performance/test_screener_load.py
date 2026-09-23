import time
import httpx
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE_URL = "http://127.0.0.1:8000"


def call_screener():
    with httpx.Client(base_url=BASE_URL) as client:
        response = client.get(
            "/screener",
            params={"sector": "IT", "min_roe": 15},  # match your route signature
        )
        response.raise_for_status()
        return response.json()


def test_screener_load():
    start = time.time()

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(call_screener) for _ in range(10)]
        results = [future.result() for future in as_completed(futures)]

    elapsed = time.time() - start
    assert elapsed <= 10, f"Load test failed: took {elapsed:.2f}s"

    for r in results:
        assert "results" in r
        assert isinstance(r["results"], list)

    print(f"All 10 screener calls completed in {elapsed:.2f} seconds")
