import argparse

from bot.logging_config import logger
from bot.orders import OrderManager


parser = argparse.ArgumentParser(
    description="Binance Futures Order CLI"
)

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", required=True, type=float)
parser.add_argument("--price", type=float)

args = parser.parse_args()

try:

    manager = OrderManager()

    response = manager.place_order(
        symbol=args.symbol,
        side=args.side,
        order_type=args.type,
        quantity=args.quantity,
        price=args.price
    )

    print("\nOrder placed successfully!")

    print("\nORDER RESPONSE")

    print(f"Order ID            : {response['orderId']}")
    print(f"Symbol              : {response['symbol']}")
    print(f"Status              : {response['status']}")
    print(f"Order Type          : {response['type']}")
    print(f"Side                : {response['side']}")
    print(f"Quantity            : {response['origQty']}")
    print(f"Executed Quantity   : {response['executedQty']}")
    print(f"Average Price       : {response['avgPrice']}")

except Exception as e:

    logger.error(
        f"Error placing order because of {e}"
    )

    print(f"\nERROR: {e}")

    exit(1)