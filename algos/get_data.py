# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 01:20:56 2021

@author: raula
"""

import connect  # call in our API data
import csv
from binance.client import Client
# https://python-binance.readthedocs.io/en/latest/  READ HERE for more func
# web socket documentation:
# https://github.com/binance/binance-spot-api-docs/blob/master/web-socket-streams.md
# create account for API keys:
# https://www.binance.com/en

# create an instant of the class
client = Client(connect.API_KEY, connect.API_SECRET)

# check all tickers
prices = client.get_all_tickers()
for price in prices:
    print(price)

# collect candle data
candles = client.get_klines(symbol='BTCUSDT',
                            interval=Client.KLINE_INTERVAL_15MINUTE)

csvfile = open('15minutes.csv', 'w', newline='')
candlestick_writer = csv.writer(csvfile, delimiter=',')

for candlestick in candles:
    print(candlestick)
    candlestick_writer.writerow(candlestick)

# collect historical candle data
candlesticks = client.get_historical_klines('BTCUSDT',
                                            Client.KLINE_INTERVAL_5MINUTE,
                                            "1 Jan, 2020", "24 May, 2020")

csvfil = open('2012-2020_candlesticks.csv', 'w', newline='')
candlesticks_writer = csv.writer(csvfil, delimiter=',')

for candlestick in candlesticks:
    print(candlestick)
    candlesticks_writer.writerow(candlestick)

csvfile.close()
