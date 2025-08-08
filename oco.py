
import time
from client import create_client
from logging_setup import logger

def place_oco(symbol, side, quantity, take_profit_price, stop_price, poll_interval=1):
    client = create_client()
    close_side = "SELL" if side.upper() == "BUY" else "BUY"
    tp = client.futures_create_order(
        symbol=symbol,
        side=close_side,
        type="LIMIT",
        timeInForce="GTC",
        price=str(take_profit_price),
        quantity=quantity
    )
    logger.info(f"Placed TP order: {tp}")
    sl = client.futures_create_order(
        symbol=symbol,
        side=close_side,
        type="STOP_MARKET",
        stopPrice=str(stop_price),
        closePosition=False,
        quantity=quantity
    )
    logger.info(f"Placed SL order: {sl}")

    tp_id = tp.get("orderId", "SIM")
    sl_id = sl.get("orderId", "SIM")

    while True:
        try:
            logger.info("SIMULATION: OCO monitoring loop tick")
            break
        except Exception:
            logger.exception("Error in OCO loop")
        time.sleep(poll_interval)
    logger.info("OCO watch ended")
