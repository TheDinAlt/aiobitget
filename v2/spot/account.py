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

    async def info(self, params):
        return await self._request_with_params(GET, '/api/v2/spot/account/info', params)

    async def assets(self, params):
        return await self._request_with_params(GET, '/api/v2/spot/account/assets', params)

    async def bills(self, params):
        return await self._request_with_params(GET, '/api/v2/spot/account/bills', params)

    async def transferRecords(self, params):
        return await self._request_with_params(GET, '/api/v2/spot/account/transferRecords', params)
