
from decimal import Decimal, ROUND_DOWN, getcontext
getcontext().prec = 28

def get_symbol_info(client, symbol):
    info = client.futures_exchange_info()
    for s in info["symbols"]:
        if s["symbol"] == symbol:
            return s
    raise ValueError(f"Symbol {symbol} not found")

def _get_filter(symbol_info, filter_type):
    for f in symbol_info["filters"]:
        if f["filterType"] == filter_type:
            return f
    return None

def round_step_size(quantity, step_size):
    q = Decimal(str(quantity))
    step = Decimal(str(step_size))
    return float((q // step) * step)

def round_price(price, tick_size):
    p = Decimal(str(price))
    tick = Decimal(str(tick_size))
    return float((p // tick) * tick)

def validate_quantity(client, symbol, quantity):
    s = get_symbol_info(client, symbol)
    lot = _get_filter(s, "LOT_SIZE")
    min_qty = Decimal(lot["minQty"])
    step = Decimal(lot["stepSize"])
    qty = Decimal(str(quantity))
    if qty < min_qty:
        raise ValueError(f"Quantity {quantity} < minQty {min_qty}")
    return round_step_size(quantity, step)

def validate_price(client, symbol, price):
    s = get_symbol_info(client, symbol)
    pf = _get_filter(s, "PRICE_FILTER")
    min_price = Decimal(pf["minPrice"])
    tick = Decimal(pf["tickSize"])
    p = Decimal(str(price))
    if p < min_price:
        raise ValueError(f"Price {price} < minPrice {min_price}")
    return round_price(price, tick)
