from bot.client import BinanceFuturesClient
from bot.validators import (validate_side,validate_order_type,validate_quantity,validate_price)
from bot.logging_config import logger

class OrderManager:
    def __init__(self):
        self.client = BinanceFuturesClient()

    def place_order(self,symbol, side, order_type, quantity, price=None):
        side = validate_side(side)

        order_type = validate_order_type(order_type)

        quantity = validate_quantity(quantity)

        price = validate_price(
            price,
            order_type
        )
        logger.info(f"Validated order for {symbol}")


        logger.info(f"Preparing {order_type} order")


        order_data = {
            "symbol": symbol.upper(),
            "side": side,
            "type": order_type,
            "quantity": quantity,
            "recvWindow": 10000
        }

        #limit checking
        if order_type == "LIMIT":
            order_data["price"] = price
            order_data["timeInForce"] = "GTC"
        response = self.client.place_order(order_data)

        logger.info(f"Order successfully sent for {symbol}")
        return response