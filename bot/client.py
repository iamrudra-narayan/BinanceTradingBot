from binance.client import Client
from binance.exceptions import BinanceAPIException
from config import Config

class BinanceFuturesClient:
    def __init__(self):
        self.api_key = Config.API_KEY
        self.api_secret = Config.API_SECRET

    def get_client(self) -> Client:
        try:
            return Client(self.api_key, self.api_secret, testnet=True) 
        except BinanceAPIException as e:
            raise Exception(f"Failed to create Binance client: {e}")