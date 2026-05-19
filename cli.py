from binance.client import Client
from dotenv import load_dotenv
import os
import argparse
import logging


logging.basicConfig(
    filename="trading.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)
parser = argparse.ArgumentParser(description='Binance Futures Order CLI working')

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", required=True, type=float)
parser.add_argument("--price", type=float)

args=parser.parse_args()
args.side=args.side.upper()

if args.side not in ['BUY', 'SELL']:
    raise ValueError("Invalid side. Must be 'BUY' or 'SELL' refer to -h for help.")
args.type=args.type.upper()

if args.type not in ['MARKET', 'LIMIT', 'STOP', 'STOP_MARKET', 'TAKE_PROFIT', 'TAKE_PROFIT_MARKET']:
    raise ValueError("Invalid type. Must be one of 'MARKET', 'LIMIT', 'STOP', 'STOP_MARKET', 'TAKE_PROFIT', 'TAKE_PROFIT_MARKET' refer to -h for help.")

if args.quantity <= 0:
    raise ValueError("Quantity must be a positive number.")

if args.type == "LIMIT":
    if args.price is None:
        raise ValueError(
            "LIMIT orders require --price"
        )

    if args.price <= 0:
        raise ValueError(
            "Price must be greater than 0"
        )
load_dotenv()

api_key = os.getenv('BINANCE_API_KEY')
api_secret = os.getenv('BINANCE_API_SECRET')
client= Client(api_key, api_secret)
client.FUTURES_URL=os.getenv('BINANCE_FUTURES_URL')
logging.info("Connected to Binance Futures Testnet")
try:
    order_data = {
        "symbol": args.symbol,
        "side": args.side,
        "type": args.type,
        "quantity": args.quantity,
        "recvWindow": 10000
    }
    logging.info(f"Sending order: {order_data}")

    if args.type == "LIMIT":
        order_data["price"] = args.price
        order_data["timeInForce"] = "GTC"
    response = client.futures_create_order(**order_data)
    print("Order placed successfully!")
    logging.info(f"Order response: {response}")
    print("\nORDER RESPONSE")

    print(f"Order ID      : {response['orderId']}")
    print(f"Symbol        : {response['symbol']}")
    print(f"Status        : {response['status']}")
    print(f"Order Type    : {response['type']}")
    print(f"Quantity      : {response['origQty']}")
    print(f"Executed Quantity  : {response['executedQty']}")
    print(f"Average Price : {response['avgPrice']}")
    
except Exception as e:
    logging.error(f"Error placing order because of {e}")
    exit(1)

