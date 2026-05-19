from binance.client import Client
from dotenv import load_dotenv
import os
import argparse
from bot.logging_config import logger
from bot.validators import (validate_side,validate_order_type,validate_quantity,validate_price)


parser = argparse.ArgumentParser(description='Binance Futures Order CLI working')

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", required=True, type=float)
parser.add_argument("--price", type=float)

args=parser.parse_args()
args.side = validate_side(args.side)

args.type = validate_order_type(
    args.type
)

args.quantity = validate_quantity(
    args.quantity
)

args.price = validate_price(
    args.price,
    args.type
)

load_dotenv()

api_key = os.getenv('BINANCE_API_KEY')
api_secret = os.getenv('BINANCE_API_SECRET')
client= Client(api_key, api_secret)
client.FUTURES_URL=os.getenv('BINANCE_FUTURES_URL')
logger.info("Connected to Binance Futures Testnet")
try:
    order_data = {
        "symbol": args.symbol,
        "side": args.side,
        "type": args.type,
        "quantity": args.quantity,
        "recvWindow": 10000
    }
    logger.info(f"Sending order: {order_data}")

    if args.type == "LIMIT":
        order_data["price"] = args.price
        order_data["timeInForce"] = "GTC"
    response = client.futures_create_order(**order_data)
    print("Order placed successfully!")
    logger.info(f"Order response: {response}")
    print("\nORDER RESPONSE")

    print(f"Order ID      : {response['orderId']}")
    print(f"Symbol        : {response['symbol']}")
    print(f"Status        : {response['status']}")
    print(f"Order Type    : {response['type']}")
    print(f"Quantity      : {response['origQty']}")
    print(f"Executed Quantity  : {response['executedQty']}")
    print(f"Average Price : {response['avgPrice']}")
    
except Exception as e:
    logger.error(f"Error placing order because of {e}")
    exit(1)

