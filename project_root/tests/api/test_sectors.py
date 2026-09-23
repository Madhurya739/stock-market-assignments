import pytest
import httpx
from src.api.main import app


@pytest.mark.asyncio
async def test_sectors_returns_exactly_11_sectors():
    """Ensure /sectors endpoint returns exactly 11 distinct sectors."""
    transport = httpx.ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/sectors")
    assert response.status_code == 200

    payload = response.json()
    assert "sectors" in payload
    # Must return exactly 11 distinct sectors
    assert len(payload["sectors"]) == 11


@pytest.mark.asyncio
async def test_sectors_it_returns_only_it_companies():
    transport = httpx.ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/sectors/IT")
    assert response.status_code == 200

    payload = response.json()
    assert "companies" in payload
    # Every returned company must belong to IT sector
    for company in payload["companies"]:
        assert company["broad_sector"].upper() == "IT"
