from fastapi import FastAPI
from src.api.routers import screener

app = FastAPI()
app.include_router(screener.router)
