from aiohttp import ClientSession

class HTTPClient:
    def __init__(self, base_url: str, api_key: str):
        self._session = ClientSession(
            base_url=base_url,
            headers = {
                'Accepts': 'application/json',
                'X-CMC_PRO_API_KEY': api_key,
            }
        )

class CMCHTTPClient(HTTPClient):
    async def get_listings(self):
        async with self._session.get("/v1/cryptocurrency/listings/latest") as response:
            result = await response.json()
            return result["data"]
        
    async def get_coin(self, coin_id: int):
        async with self._session.get(
            "/v2/cryptocurrency/quotes/latest",
            params={"id": coin_id}
            ) as response:
            result = await response.json()
            return result["data"][str(coin_id)]