
from client import create_client
from logging_setup import logger
from validators import validate_quantity

def place_market_order(symbol, side, quantity):
    client = create_client()
    try:
        qty = validate_quantity(client, symbol, quantity)
        logger.info(f"Attempting MARKET order {side} {symbol} qty={qty}")
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=qty
        )
        logger.info(f"Order result: {order}")
        return order
    except Exception as e:
        logger.exception("Market order failed")
        raise
