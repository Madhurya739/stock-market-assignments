import pytest
import httpx
from src.api.main import app


@pytest.mark.asyncio
async def test_health_endpoint_returns_ok_and_all_tables():
    # Mount FastAPI app directly into httpx using ASGITransport
    transport = httpx.ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/api/v1/health/")  # must match your router path
    assert response.status_code == 200

    payload = response.json()
    assert payload["status"] == "ok"

    expected_tables = {
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
    }
    assert set(payload["db_row_counts"].keys()) == expected_tables
    for table in expected_tables:
        assert isinstance(payload["db_row_counts"][table], (int, type(None)))
