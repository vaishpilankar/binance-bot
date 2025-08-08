
import os
from dotenv import load_dotenv
from binance.client import Client

load_dotenv()

def create_client():
    simulated = os.getenv("SIMULATED_MODE", "true").lower() in ("1", "true", "yes")
    if simulated:
        class DummyClient:
            def futures_create_order(self, **kwargs):
                print("[SIMULATION] futures_create_order called:", kwargs)
                return {"status": "SIMULATED", "order": kwargs}
            def futures_exchange_info(self):
                return {
                    "symbols": [
                        {
                            "symbol": "BTCUSDT",
                            "filters": [
                                {"filterType": "LOT_SIZE", "minQty": "0.001", "stepSize": "0.001"},
                                {"filterType": "PRICE_FILTER", "minPrice": "1", "tickSize": "0.1"}
                            ]
                        }
                    ]
                }
        return DummyClient()
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")
    testnet = os.getenv("BINANCE_TESTNET", "true").lower() in ("1","true","yes")
    if not api_key or not api_secret:
        raise RuntimeError("Set API keys in .env or enable SIMULATED_MODE")
    client = Client(api_key, api_secret, testnet=testnet)
    if testnet:
        client.API_URL = "https://testnet.binancefuture.com"
    return client
