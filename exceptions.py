# coding=utf-8
from aiohttp import ClientResponse

class BitgetAPIException(Exception):

    def __init__(self, resp: ClientResponse, resp_json: ClientResponse.json):
        self.code = 0
        if "code" in resp_json.keys() and "msg" in resp_json.keys():
            self.code = resp_json['code']
            self.message = resp_json['msg']
        else:
            self.code = 'Please wait a moment'
            self.message = 'Maybe something is wrong'

        self.status_code = resp.status
        self.resp = resp
        self.request = getattr(resp, 'request', None)

    def __str__(self):  # pragma: no cover
        return 'API Request Error(code=%s): %s' % (self.code, self.message)



class BitgetRequestException(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return 'BitgetRequestException: %s' % self.message



class BitgetParamsException(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return 'BitgetParamsException: %s' % self.message
