#!/usr/bin/env python
import sys
from stocker import Stocker

if __name__ == "__main__":
    args = sys.argv[1:]
    symbol = args[0]
    
    stocker = Stocker()
    
    price, time_of_price = stocker.get_stock_price(symbol)

    print "{symbol}: ${price}, Time of price: {time_of_price}".format(symbol=symbol, price=price, time_of_price=time_of_price)



