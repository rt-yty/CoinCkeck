from fastapi import FastAPI
from src.http_client import CMCHTTPClient
from src.config import settings
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

cmc_client = CMCHTTPClient(
    base_url="https://pro-api.coinmarketcap.com",
    api_key=settings.CMC_API_KEY
)

@app.get("/cryptocurrencies")
async def get_cryptocurrencies():
    return await cmc_client.get_listings()

@app.get("/cryptocurrencies/{coin_id}")
async def get_coin(coin_id: int):
    return await cmc_client.get_coin(coin_id)