def validate_side(side):
    side = side.upper()

    if side not in ["BUY", "SELL"]:
        raise ValueError(
            "Side must be BUY or SELL only two options available"
        )

    return side

def validate_order_type(order_type):
    order_type = order_type.upper()

    valid_types = [
        "MARKET",
        "LIMIT",
        "STOP",
        "STOP_MARKET",
        "TAKE_PROFIT",
        "TAKE_PROFIT_MARKET"
    ]

    if order_type not in valid_types:
        raise ValueError(
            f"Invalid order type: {order_type}"
        )

    return order_type

def validate_quantity(quantity):
    if quantity <= 0:
        raise ValueError(
            "Quantity should be greater than 0"
        )

    return quantity

def validate_price(price, order_type):
    if order_type == "LIMIT":

        if price is None:
            raise ValueError(
                "Limit orders have to have a price"
            )

        if price <= 0:
            raise ValueError(
                "Purchase of something for free or a negative price doesn't make sense"
            )

    return price