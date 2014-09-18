from stock_api import StockAPI
import requests
import time

class YahooStockAPI(StockAPI):
    
    def __init__(self):
        super(YahooStockAPI, self).__init__("YahooStockAPI") 

    def get_stock_price(self, symbol):
        response = requests.get("http://download.finance.yahoo.com/d/quotes.csv?s={symbol}&f=sl1po".format(symbol=symbol))
        string = response.text
        if "N/A" in string:
            raise Exception("Invalid symbol {symbol}".format(symbol=symbol))
        tokens = string.split(",")
        price, price_last_closed, price_opened = map(lambda x: float(str(x).strip()), tokens[1:])
        return price, time.time()

