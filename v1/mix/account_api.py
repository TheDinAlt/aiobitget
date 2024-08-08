from aiohttp import ClientSession
from aiobitget.client import Client
from aiobitget.consts import GET, POST


class AccountApi(Client):
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

    async def account(self, params):
        return await self._request_with_params(GET, '/api/mix/v1/account/account', params)

    async def accounts(self, params):
        return await self._request_with_params(GET, '/api/mix/v1/account/accounts', params)

    async def setLeverage(self, params):
        return await self._request_with_params(POST, '/api/mix/v1/account/setLeverage', params)

    async def setMargin(self, params):
        return await self._request_with_params(POST, '/api/mix/v1/account/setMargin', params)

    async def setMarginMode(self, params):
        return await self._request_with_params(POST, '/api/mix/v1/account/setMarginMode', params)

    async def setPositionMode(self, params):
        return await self._request_with_params(POST, '/api/mix/v1/account/setPositionMode', params)

    async def singlePosition(self, params):
        return await self._request_with_params(GET, '/api/mix/v1/position/singlePosition', params)

    async def allPosition(self, params):
        return await self._request_with_params(GET, '/api/mix/v1/position/allPosition', params)
