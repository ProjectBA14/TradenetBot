from binance.client import Client
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('BINANCE_API_KEY')
api_secret = os.getenv('BINANCE_API_SECRET')
client= Client(api_key, api_secret)
client.FUTURES_URL=os.getenv('BINANCE_FUTURES_URL')

response=client.futures_create_order(
    symbol='BTCUSDT',
    side='BUY',
    type='MARKET',
    quantity=0.001
)

print("\nORDER RESPONSE")

print(f"Order ID      : {response['orderId']}")
print(f"Symbol        : {response['symbol']}")
print(f"Status        : {response['status']}")
print(f"Order Type    : {response['type']}")
print(f"Quantity      : {response['origQty']}")
print(f"Executed Quantity  : {response['executedQty']}")
print(f"Average Price : {response['avgPrice']}")