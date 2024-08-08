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
        return await self._request_with_params(POST, '/api/v2/mix/order/place-order', params)

    async def clickBackhand(self, params):
        return await self._request_with_params(POST, '/api/v2/mix/order/click-backhand', params)

    async def batchPlaceOrder(self, params):
        return await self._request_with_params(POST, '/api/v2/mix/order/batch-place-order', params)

    async def cancelOrder(self, params):
        return await self._request_with_params(POST, '/api/v2/mix/order/cancel-order', params)

    async def batchCancelOrders(self, params):
        return await self._request_with_params(POST, '/api/v2/mix/order/batch-cancel-orders', params)

    async def closePositions(self, params):
        return await self._request_with_params(POST, '/api/v2/mix/order/close-positions', params)

    async def ordersHistory(self, params):
        return await self._request_with_params(GET, '/api/v2/mix/order/orders-history', params)

    async def ordersPending(self, params):
        return await self._request_with_params(GET, '/api/v2/mix/order/orders-pending', params)

    async def detail(self, params):
        return await self._request_with_params(GET, '/api/v2/mix/order/detail', params)

    async def fills(self, params):
        return await self._request_with_params(GET, '/api/v2/mix/order/fills', params)

    async def placePlanOrder(self, params):
        return await self._request_with_params(POST, '/api/v2/mix/order/place-plan-order', params)

    async def cancelPlanOrder(self, params):
        return await self._request_with_params(POST, '/api/v2/mix/order/cancel-plan-order', params)

    async def ordersPlanPending(self, params):
        return await self._request_with_params(GET, '/api/v2/mix/order/orders-plan-pending', params)

    async def ordersPlanHistory(self, params):
        return await self._request_with_params(GET, '/api/v2/mix/order/orders-plan-history', params)

    async def traderOrderClosePositions(self, params):
        return await self._request_with_params(POST, '/api/v2/copy/mix-trader/order-close-positions', params)

    async def traderOrderCurrentTrack(self, params):
        return await self._request_with_params(GET, '/api/v2/copy/mix-trader/order-current-track', params)

    async def traderOrderHistoryTrack(self, params):
        return await self._request_with_params(GET, '/api/v2/copy/mix-trader/order-history-track', params)

    async def followerClosePositions(self, params):
        return await self._request_with_params(POST, '/api/v2/copy/mix-follower/close-positions', params)

    async def followerQueryCurrentOrders(self, params):
        return await self._request_with_params(GET, '/api/v2/copy/mix-follower/query-current-orders', params)

    async def followerQueryHistoryOrders(self, params):
        return await self._request_with_params(GET, '/api/v2/copy/mix-follower/query-history-orders', params)
