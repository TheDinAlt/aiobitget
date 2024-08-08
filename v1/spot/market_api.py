from aiohttp import ClientSession
from aiobitget.client import Client
from aiobitget.consts import GET


class MarketApi(Client):
    def __init__(self, 
                 api_key: str, 
                 api_secret_key: str, 
                 passphrase: str, 
                 session: ClientSession = None,
                 use_server_time: bool = False, 
                 first: bool = False):
        super().__init__(api_key, 
                         api_secret_key, 
                         passphrase,
                         session=session,
                         use_server_time=use_server_time, 
                         first=first)

    async def currencies(self, params):
        return await self._request_with_params(GET, '/api/spot/v1/public/currencies', params)

    async def products(self, params):
        return await self._request_with_params(GET, '/api/spot/v1/public/products', params)

    async def product(self, params):
        return await self._request_with_params(GET, '/api/spot/v1/public/product', params)

    async def fills(self, params):
        return await self._request_with_params(GET, '/api/spot/v1/market/fills', params)

    async def depth(self, params):
        return await self._request_with_params(GET, '/api/spot/v1/market/depth', params)

    async def ticker(self, params):
        return await self._request_with_params(GET, '/api/spot/v1/market/ticker', params)

    async def tickers(self, params):
        return await self._request_with_params(GET, '/api/spot/v1/market/tickers', params)

    async def candles(self, params):
        return await self._request_with_params(GET, '/api/spot/v1/market/candles', params)
