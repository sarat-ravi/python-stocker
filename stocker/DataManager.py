import time
from stocker.realtime.RealtimeDataManager import RealTimeDataManager
from stocker.historic.HistoricDataManager import HistoricDataManager

class DataManager(object):
    '''
    classdocs
    '''
    
    REALTIME_THRESHOLD = 60 * 1000;

    def __init__(self):
        '''
        Constructor
        '''
        self.realtime_data_manager = RealTimeDataManager()
        self.historic_data_manager = HistoricDataManager()
        
    def get_stock_price(self, symbol, timestamp=None):
        current_time = time.time()
        if timestamp == None:
            timestamp = current_time
            
        if current_time - timestamp <= DataManager.REALTIME_THRESHOLD:
            # this means we are live.
            price, time_of_price = self.realtime_data_manager.get_stock_price(symbol)
            return price, time_of_price
        else:
            # this means we are not live, so need to dig through historic data.
            price, time_of_price = self.historic_data_manager.get_stock_price(symbol, timestamp)
            return price, time_of_price
            
        