from fastapi import FastAPI
from src.http_client import CMCHTTPClient
from src.config import settings

app = FastAPI()

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