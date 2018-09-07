import ccxt
import datetime
import time
import math
# import pandas as pd
import numpy as np
import pprint

exchange_id = 'okex'
exchange_class = getattr(ccxt, exchange_id)
exchange = exchange_class({
    'apiKey': 'YOUR_API_KEY',
    'secret': 'YOUR_SECRET',
    'timeout': 30000,
    'enableRateLimit': True,
})


# ===== Visualise market depth =====
def order_book(exchange, symbol, limit):
    # exchange = getattr(ccxt, exchange)()
    # exchange.load_markets()
    data = exchange.fetch_order_book(symbol,limit)
    bid = data['bids'][0][0] if len(data['bids']) > 0 else None
    ask = data['asks'][0][0] if len(data['asks']) > 0 else None
    return bid, ask



# ======== Details of Open & Closed Trades =========
def trade_details(symbol):
    print("Closed Orders:")
    pprint.pprint(exchange.fetch_closed_orders(symbol))

    print("Open Orders:")
    pprint.pprint(exchange.fetch_open_orders(symbol))


# ==== Get Balance amounts left on exchange =====
def exchange_balances():
    balance = exchange.fetch_balance()
    print 'Exchange Balance:\n', balance
