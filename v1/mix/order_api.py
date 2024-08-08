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
        return await self._request_with_params(POST, '/api/mix/v1/order/placeOrder', params)

    async def batchPlaceOrder(self, params):
        return await self._request_with_params(POST, '/api/mix/v1/order/batch-orders', params)

    async def cancelOrder(self, params):
        return await self._request_with_params(POST, '/api/mix/v1/order/cancel-order', params)

    async def batchCancelOrders(self, params):
        return await self._request_with_params(POST, '/api/mix/v1/order/cancel-batch-orders', params)

    async def ordersHistory(self, params):
        return await self._request_with_params(GET, '/api/mix/v1/order/history', params)

    async def ordersPending(self, params):
        return await self._request_with_params(GET, '/api/mix/v1/order/current', params)

    async def fills(self, params):
        return await self._request_with_params(GET, '/api/mix/v1/order/fills', params)

    async def placePlanOrder(self, params):
        return await self._request_with_params(POST, '/api/mix/v1/plan/placePlan', params)

    async def cancelPlan(self, params):
        return await self._request_with_params(POST, '/api/mix/v1/plan/cancelPlan', params)

    async def currentPlan(self, params):
        return await self._request_with_params(GET, '/api/mix/v1/plan/currentPlan', params)

    async def historyPlan(self, params):
        return await self._request_with_params(GET, '/api/mix/v1/plan/historyPlan', params)

    async def traderCloseOrder(self, params):
        return await self._request_with_params(POST, '/api/mix/v1/trace/closeTrackOrder', params)

    async def traderOrderCurrentTrack(self, params):
        return await self._request_with_params(GET, '/api/mix/v1/trace/currentTrack', params)

    async def traderOrderHistoryTrack(self, params):
        return await self._request_with_params(GET, '/api/mix/v1/trace/historyTrack', params)

    async def followerCloseByTrackingNo(self, params):
        return await self._request_with_params(POST, '/api/mix/v1/trace/followerCloseByTrackingNo', params)

    async def followerQueryCurrentOrders(self, params):
        return await self._request_with_params(GET, '/api/mix/v1/trace/followerOrder', params)

    async def followerQueryHistoryOrders(self, params):
        return await self._request_with_params(GET, '/api/mix/v1/trace/followerHistoryOrders', params)
