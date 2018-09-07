import ccxt
import datetime
import time
import math
# import pandas as pd
import numpy as np
import pprint
from historical_data import exchange_data
import oms

# ==== Initial exchange parameters =====
symbol = str('BTC/USD')
symbol_list = ['BTC/USD','ETH/USD']
timeframe = str('1d')
# exchange = str('okex')
start_date = str('2018-01-01')
get_data = True
reqd_balance = 1000


exchange_id = 'kraken'
exchange_class = getattr(ccxt, exchange_id)
exchange = exchange_class({
    'apiKey': 'YOUR_API_KEY',
    'secret': 'YOUR_SECRET',
    'timeout': 30000,
    'enableRateLimit': True,
})

data = exchange_data(exchange_id,symbol,timeframe='1m',since=start_date)
def initiate_trade(exchange,symbol):
    ema_short = data['Close'].ewm(span=100, adjust=False).mean()
    bid, ask = oms.order_book(exchange,symbol,5)
    price = (bid+ask)/2

    if price > ema_short:
        exchange.create_limit_buy_order(symbol,1,)

# =================INCOMPLETE CODE ===================
