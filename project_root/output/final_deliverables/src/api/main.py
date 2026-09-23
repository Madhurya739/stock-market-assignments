from fastapi import FastAPI
from src.api.routers import health, companies, screener, sectors

app = FastAPI()

app.include_router(health.router, prefix="/api/v1")
app.include_router(companies.router)
app.include_router(screener.router)
app.include_router(sectors.router)
