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
        return await self._request_with_params(POST, '/api/spot/v1/trade/orders', params)

    async def batchOrders(self, params):
        return await self._request_with_params(POST, '/api/spot/v1/trade/batch-orders', params)

    async def cancelOrder(self, params):
        return await self._request_with_params(POST, '/api/spot/v1/trade/cancel-order', params)

    async def batchCancelOrder(self, params):
        return await self._request_with_params(POST, '/api/spot/v1/trade/cancel-batch-orders', params)

    async def openOrders(self, params):
        return await self._request_with_params(GET, '/api/spot/v1/trade/open-orders', params)

    async def historyOrders(self, params):
        return await self._request_with_params(GET, '/api/spot/v1/trade/history', params)

    async def fills(self, params):
        return await self._request_with_params(GET, '/api/spot/v1/trade/fills', params)

    async def placePlanOrder(self, params):
        return await self._request_with_params(POST, '/api/spot/v1/plan/placePlan', params)

    async def cancelPlanOrder(self, params):
        return await self._request_with_params(POST, '/api/spot/v1/plan/cancelPlan', params)

    async def currentPlanOrder(self, params):
        return await self._request_with_params(POST, '/api/spot/v1/plan/currentPlan', params)

    async def historyPlanOrder(self, params):
        return await self._request_with_params(POST, '/api/spot/v1/plan/historyPlan', params)

    async def traderOrderCloseTracking(self, params):
        return await self._request_with_params(POST, '/api/spot/v1/trace/order/closeTrackingOrder', params)

    async def traderOrderCurrentTrack(self, params):
        return await self._request_with_params(POST, '/api/spot/v1/trace/order/orderCurrentList', params)

    async def traderOrderHistoryTrack(self, params):
        return await self._request_with_params(GET, '/api/spot/v1/trace/order/orderHistoryList', params)
