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

    async def contracts(self, params):
        return await self._request_with_params(GET, '/api/v2/mix/market/contracts', params)

    async def orderbook(self, params):
        return await self._request_with_params(GET, '/api/v2/mix/market/orderbook', params)
    
    async def ticker(self, params):
        return await self._request_with_params(GET, '/api/v2/mix/market/ticker', params)

    async def tickers(self, params):
        return await self._request_with_params(GET, '/api/v2/mix/market/tickers', params)

    async def fills(self, params):
        return await self._request_with_params(GET, '/api/v2/mix/market/fills', params)

    async def candles(self, params):
        return await self._request_with_params(GET, '/api/v2/mix/market/candles', params)
