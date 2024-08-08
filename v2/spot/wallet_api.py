from aiohttp import ClientSession
from aiobitget.client import Client
from aiobitget.consts import GET, POST


class WalletApi(Client):
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

    async def transfer(self, params):
        return await self._request_with_params(POST, '/api/v2/spot/wallet/transfer', params)

    async def depositAddress(self, params):
        return await self._request_with_params(GET, '/api/v2/spot/wallet/deposit-address', params)

    async def withdrawal(self, params):
        return await self._request_with_params(POST, '/api/v2/spot/wallet/withdrawal', params)

    async def withdrawalRecords(self, params):
        return await self._request_with_params(GET, '/api/v2/spot/wallet/withdrawal-records', params)

    async def depositRecords(self, params):
        return await self._request_with_params(GET, '/api/v2/spot/wallet/deposit-records', params)
