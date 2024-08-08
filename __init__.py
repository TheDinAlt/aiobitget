from typing import Literal, List
from aiohttp import ClientSession

class BitGetClient:
    def __init__(self, 
                 api_key, 
                 api_secret, 
                 passphrase,
                 version: Literal["v1", "v2"] = "v2",
                 mode: Literal["mix", "spot"] = "mix",
                 modules: List[Literal["account", "market", "order, wallet"]] = ["account", "market", "order"],
                 use_server_time: bool = True, 
                 first: bool = False):
        
        self.session = ClientSession(headers=dict(ContentType='application/json'))

        if "account" in modules:
            match version, mode:
                case "v1", "mix":
                    from .v1.mix.account_api import AccountApi
                case "v1", "spot":
                    from .v1.spot.account_api import AccountApi
                case "v2", "mix":
                    from .v2.mix.account_api import AccountApi
                case "v2", "spot":
                    from .v2.spot.account_api import AccountApi
            self.account = AccountApi(api_key, 
                                      api_secret,
                                      passphrase,
                                      session=self.session,
                                      use_server_time=use_server_time, 
                                      first=first)
            
        if "market" in modules:
            match version, mode:
                case "v1", "mix":
                    from .v1.mix.market_api import MarketApi
                case "v1", "spot":
                    from .v1.spot.market_api import MarketApi
                case "v2", "mix":
                    from .v2.mix.market_api import MarketApi
                case "v2", "spot":
                    from .v2.spot.market_api import MarketApi
            self.market = MarketApi(api_key,
                                    api_secret,
                                    passphrase,
                                    session=self.session,
                                    use_server_time=use_server_time,
                                    first=first)
            
        if "order" in modules:
            match version, mode:
                case "v1", "mix":
                    from .v1.mix.order_api import OrderApi
                case "v1", "spot":
                    from .v1.spot.order_api import OrderApi
                case "v2", "mix":
                    from .v2.mix.order_api import OrderApi
                case "v2", "spot":
                    from .v2.spot.order_api import OrderApi
            self.order = OrderApi(api_key,
                                  api_secret,
                                  passphrase,
                                  session=self.session,
                                  use_server_time=use_server_time,
                                  first=first)
            
        if "wallet" in modules and mode == "spot":
            match version, mode:
                case "v1", "spot":
                    from .v1.spot.wallet_api import WalletApi
                case "v2", "spot":
                    from .v2.spot.wallet_api import WalletApi
            self.wallet = WalletApi(api_key,
                                    api_secret,
                                    passphrase,
                                    session=self.session,
                                    use_server_time=use_server_time,
                                    first=first)
            
    async def close_client(self):
        await self.session.close()
