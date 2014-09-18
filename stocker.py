#!/usr/bin/env python
import sys
from stocker.realtime.stockapi import YahooStockAPI
from stocker.realtime import RealtimeDataManager

if __name__ == "__main__":
    args = sys.argv[1:]
    symbol = args[0]

    stock_api = YahooStockAPI()
    price = stock_api.get_stock_price(symbol)

    print "Using {api}".format(api=stock_api)
    print "{symbol}: ${price}".format(symbol=symbol, price=price)



