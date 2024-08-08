from aiohttp import ClientSession
from aiobitget.client import Client
from aiobitget.consts import GET, POST


class OrderApi(Client):
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

    async def placeOrder(self, params):
        return await self._request_with_params(POST, '/api/v2/spot/trade/place-order', params)

    async def batchOrders(self, params):
        return await self._request_with_params(POST, '/api/v2/spot/trade/batch-orders', params)

    async def cancelOrder(self, params):
        return await self._request_with_params(POST, '/api/v2/spot/trade/cancel-order', params)

    async def batchCancelOrder(self, params):
        return await self._request_with_params(POST, '/api/v2/spot/trade/batch-cancel-order', params)

    async def historyOrders(self, params):
        return await self._request_with_params(GET, '/api/v2/spot/trade/unfilled-orders', params)

    async def historyOrders(self, params):
        return await self._request_with_params(GET, '/api/v2/spot/trade/history-orders', params)

    async def fills(self, params):
        return await self._request_with_params(GET, '/api/v2/spot/trade/fills', params)

    async def placePlanOrder(self, params):
        return await self._request_with_params(POST, '/api/v2/spot/trade/place-plan-order', params)

    async def modifyPlanOrder(self, params):
        return await self._request_with_params(POST, '/api/v2/spot/trade/modify-plan-order', params)

    async def cancelPlanOrder(self, params):
        return await self._request_with_params(POST, '/api/v2/spot/trade/cancel-plan-order', params)

    async def currentPlanOrder(self, params):
        return await self._request_with_params(GET, '/api/v2/spot/trade/current-plan-order', params)

    async def historyPlanOrder(self, params):
        return await self._request_with_params(GET, '/api/v2/spot/trade/history-plan-order', params)

    async def traderOrderCloseTracking(self, params):
        return await self._request_with_params(POST, '/api/v2/copy/spot-trader/order-close-tracking', params)

    async def traderOrderCurrentTrack(self, params):
        return await self._request_with_params(GET, '/api/v2/copy/spot-trader/order-current-track', params)

    async def traderOrderHistoryTrack(self, params):
        return await self._request_with_params(GET, '/api/v2/copy/spot-trader/order-history-track', params)
