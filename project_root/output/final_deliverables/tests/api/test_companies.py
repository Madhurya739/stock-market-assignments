import pytest
import httpx
from src.api.main import app


@pytest.mark.asyncio
async def test_list_companies_returns_92_records():
    transport = httpx.ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/companies")
    assert response.status_code == 200

    payload = response.json()
    assert "companies" in payload
    assert payload["count"] == 92
    assert len(payload["companies"]) == 92


@pytest.mark.asyncio
async def test_get_company_tcs_returns_correct_data():
    transport = httpx.ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/companies/TCS")
    assert response.status_code == 200

    payload = response.json()
    # Adjust keys to match your schema
    assert payload["company_name"] == "Tata Consultancy Services"
    assert payload["ticker"] == "TCS"
    assert payload["broad_sector"] == "IT"


@pytest.mark.asyncio
async def test_get_company_invalid_returns_404():
    transport = httpx.ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/companies/INVALID")
    assert response.status_code == 404
