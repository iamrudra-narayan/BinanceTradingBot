from binance.client import Client
from bot.client import BinanceFuturesClient
from binance.exceptions import BinanceAPIException
from bot.validators import Validators

binance_futures_client = BinanceFuturesClient()
validators = Validators()

class BinanceOrderService:
    def __init__(self):
        self.client: Client = binance_futures_client.get_client()

    def place_futures_order(self, symbol: str, side: str, order_type: str, quantity: float, price=None):
        try:
            params = {
                "symbol": symbol.upper(),
                "side": side.upper(),
                "type": order_type.upper(),
                "quantity": quantity,
            }
            if order_type.upper() == "LIMIT":
                params["price"] = price
                params["timeInForce"] = "GTC"

            response = self.client.futures_create_order(**params)
            return response
        except BinanceAPIException as e:
            return {"error": str(e)}