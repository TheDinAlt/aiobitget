import traceback
import asyncio
from aiohttp import ClientSession, ClientResponse
import json
from . import consts as c, utils, exceptions
    

class Client:
    def __init__(self, 
                 api_key: str, 
                 api_secret_key: str, 
                 passphrase: str, 
                 session: ClientSession = None, 
                 use_server_time = False, 
                 first=False):
        self.loop = asyncio.get_running_loop()
        self.API_KEY = api_key
        self.API_SECRET_KEY = api_secret_key
        self.PASSPHRASE = passphrase
        self.use_server_time = use_server_time
        self.first = first
        self.session = session if session else ClientSession(headers=dict(ContentType='application/json'))

    
    async def _close(self):
        await self.session.close()


    async def _request(self, method, request_path, params, cursor=False):
        if method == c.GET:
            request_path = request_path + utils.parse_params_to_str(params)
        # url
        url = c.API_URL + request_path

        # sign & header
        if self.use_server_time:
            timestamp = await self._get_timestamp()
        else:
            timestamp = utils.get_timestamp()

        body = json.dumps(params) if method == c.POST else ""
        sign = utils.sign(utils.pre_hash(timestamp, method, request_path, str(body)), self.API_SECRET_KEY)
        if c.SIGN_TYPE == c.RSA:
            sign = utils.signByRSA(utils.pre_hash(timestamp, method, request_path, str(body)), self.API_SECRET_KEY)
        header = utils.get_header(self.API_KEY, sign, timestamp, self.PASSPHRASE)

        if self.first:
            print("url:", url)
            print("method:", method)
            print("body:", body)
            print("headers:", header)
            # print("sign:", sign)
            self.first = False

        # send request
        try:
            request = getattr(self.session, method.lower())
            request: ClientSession
            async with request(url, data=body, headers=header) as resp:
                resp: ClientResponse
                resp_status = resp.status
                resp_headers = resp.headers
                resp_json = await resp.json()
                resp_text = await resp.text()

            #await self.session.close()

            # exception handle
            if not str(resp_status).startswith('2'):
                raise exceptions.BitgetAPIException(resp, resp_json)
            try:
                if cursor:
                    try:
                        r = dict(
                            before=resp_headers['OK-BEFORE'],
                            after=resp_headers['OK-AFTER']
                        )
                    except:
                        pass
                    return resp_json, r
                else:
                    return resp_json

            except ValueError:
                raise exceptions.BitgetRequestException('Invalid Response: %s' % resp_text)
        except:
            print(traceback.format_exc())

    async def _request_without_params(self, method, request_path):
        return await self._request(method, request_path, {})

    async def _request_with_params(self, method, request_path, params, cursor=False):
        return await self._request(method, request_path, params, cursor)

    async def _get_timestamp(self):
        url = c.API_URL + c.SERVER_TIMESTAMP_URL
        try:
            async with self.session.get(url=url) as resp:
                resp_status = resp.status
                resp_json = await resp.json()

            #await self.session.close()

            if resp_status == 200:
                return resp_json['data']['serverTime']
            else:
                return ""
        except:
            print(traceback.format_exc())
