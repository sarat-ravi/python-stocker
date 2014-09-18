'''
Created on Sep 17, 2014

@author: saratt
'''
from stocker.DataManager import DataManager

class Stocker(object):
    
    def __init__(self):
        self.data_manager = DataManager()
        
    def get_stock_price(self, symbol, timestamp=None):
        return self.data_manager.get_stock_price(symbol, timestamp)