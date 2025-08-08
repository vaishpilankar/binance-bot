
from client import create_client
from logging_setup import logger
from validators import validate_quantity, validate_price

def place_limit_order(symbol, side, quantity, price, timeInForce="GTC"):
    client = create_client()
    try:
        qty = validate_quantity(client, symbol, quantity)
        pr = validate_price(client, symbol, price)
        logger.info(f"Attempting LIMIT order {side} {symbol} qty={qty} price={pr}")
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            timeInForce=timeInForce,
            price=str(pr),
            quantity=qty
        )
        logger.info(f"Order result: {order}")
        return order
    except Exception as e:
        logger.exception("Limit order failed")
        raise
