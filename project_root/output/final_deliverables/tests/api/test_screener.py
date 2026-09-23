import pytest
import httpx
from src.api.main import app


@pytest.mark.asyncio
async def test_screener_min_roe_returns_only_high_roe_companies():
    transport = httpx.ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/screener", params={"min_roe": 15})
    assert response.status_code == 200

    payload = response.json()
    assert "companies" in payload
    # Every returned company must satisfy ROE >= 15
    for company in payload["companies"]:
        assert company["roe"] >= 15


@pytest.mark.asyncio
async def test_screener_invalid_parameter_returns_400():
    transport = httpx.ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/screener", params={"invalid_param": 123})
    assert response.status_code == 400
