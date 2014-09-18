'''
Created on Sep 17, 2014

@author: saratt
'''
from stocker.realtime.stockapi import YahooStockAPI

class RealTimeDataManager(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.stock_api = YahooStockAPI()
        
    def get_stock_price(self, symbol):
        """
        Returns the real time stock price and the time of the price
        """
        return self.stock_api.get_stock_price(symbol)
        
        
        