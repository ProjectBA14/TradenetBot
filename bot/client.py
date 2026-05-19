from binance.client import Client
from dotenv import load_dotenv

import os

from bot.logging_config import logger

load_dotenv()

class BinanceFuturesClient:
    def __init__(self):
        api_key = os.getenv('BINANCE_API_KEY')
        api_secret = os.getenv('BINANCE_API_SECRET')
        self.client = Client(api_key, api_secret)
        self.client.FUTURES_URL = os.getenv('BINANCE_FUTURES_URL')
        logger.info("Connected to Binance Futures Testnet")
    def place_order(self, order_data):
        logger.info(f"Sending order: {order_data}")
        response = self.client.futures_create_order(**order_data)
        logger.info(f"Order response: {response}")
        return response            