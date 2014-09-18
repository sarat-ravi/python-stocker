

class StockAPI(object):

    def __init__(self, name):
        self.name = name;

    def get_stock_price(self, symbol):
        raise NotImplementedError

    def __repr__(self):
        return self.name
