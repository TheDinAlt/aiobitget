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
        return await self._request_with_params(GET, '/api/v2/mix/account/account', params)

    async def accounts(self, params):
        return await self._request_with_params(GET, '/api/v2/mix/account/accounts', params)

    async def setLeverage(self, params):
        return await self._request_with_params(POST, '/api/v2/mix/account/set-leverage', params)

    async def setMargin(self, params):
        return await self._request_with_params(POST, '/api/v2/mix/account/set-margin', params)

    async def setMarginMode(self, params):
        return await self._request_with_params(POST, '/api/v2/mix/account/set-margin-mode', params)

    async def setPositionMode(self, params):
        return await self._request_with_params(POST, '/api/v2/mix/account/set-position-mode', params)

    async def openCount(self, params):
        return await self._request_with_params(GET, '/api/v2/mix/account/open-count', params)

    async def singlePosition(self, params):
        return await self._request_with_params(GET, '/api/v2/mix/position/single-position', params)

    async def allPosition(self, params):
        return await self._request_with_params(GET, '/api/v2/mix/position/all-position', params)
