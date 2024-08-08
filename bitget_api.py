#!/usr/bin/python
from aiobitget.client import Client
from aiobitget.consts import GET, POST
from aiohttp import ClientSession


class BitgetApi(Client):
    def __init__(self, 
                 api_key, 
                 api_secret_key, 
                 passphrase,
                 session: ClientSession = None,
                 use_server_time: bool = False, 
                 first: bool = False):
        super().__init__(self, 
                         api_key, 
                         api_secret_key, 
                         passphrase, 
                         session=session,
                         use_server_time=use_server_time, 
                         first=first)

    async def post(self, request_path, params):
        return await self._request_with_params(POST, request_path, params)

    async def get(self, request_path, params):
        return await self._request_with_params(GET, request_path, params)
