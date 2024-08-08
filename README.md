# aiobitget
Full asynchronous Python SDK for Bitget Exchange public API based on **[Bitget Open API V3 SDK](https://github.com/BitgetLimited/v3-bitget-api-sdk)**

## Quickstart
```python
import asyncio

from aiobitget import BitGetClient


async def main():
    bg = BitGetClient(
        api_key="<YOUR_API_KEY>",
        api_secret="<YOUR_API_SECRET>",
        passphrase="<YOUR_PASSPHRASE>",
    )
    resp = await bg.account.account(
        params=dict(
            symbol="BTCUSDT",
            productType="USDT-FUTURES",
            marginCoin="USDT"
            ))
    print(resp)
    await bg.close_client()

asyncio.run(main())
```

## Task list
- [ ] add websocket support
## Contacts
**Telegram:** [@TheDinAlt](https://t.me/TheDinAlt)

`with 💜 by TheDinAlt`
