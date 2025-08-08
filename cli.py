
import click
from market_orders import place_market_order
from limit_orders import place_limit_order

@click.group()
def cli():
    pass

@cli.command()
@click.argument('symbol')
@click.argument('side')
@click.argument('qty', type=float)
def market(symbol, side, qty):
    try:
        res = place_market_order(symbol.upper(), side.upper(), qty)
        print("Order response:", res)
    except Exception as e:
        print("Error:", e)

@cli.command()
@click.argument('symbol')
@click.argument('side')
@click.argument('qty', type=float)
@click.argument('price', type=float)
def limit(symbol, side, qty, price):
    try:
        res = place_limit_order(symbol.upper(), side.upper(), qty, price)
        print("Order response:", res)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    cli()
