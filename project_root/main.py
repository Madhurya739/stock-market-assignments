from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import routers as a package
from routers import (
    companies,
    screener,
    sectors,
    peers,
    valuation,
    portfolio,
    documents,
    health,
)

app = FastAPI(title="Modular FastAPI App", version="1.0")

# CORS middleware (internal use only)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers with /api/v1 prefix
app.include_router(companies.router, prefix="/api/v1")
app.include_router(screener.router, prefix="/api/v1")
app.include_router(sectors.router, prefix="/api/v1")
app.include_router(peers.router, prefix="/api/v1")
app.include_router(valuation.router, prefix="/api/v1")
app.include_router(portfolio.router, prefix="/api/v1")
app.include_router(documents.router, prefix="/api/v1")
app.include_router(health.router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "FastAPI server with /api/v1 routers is running!"}
