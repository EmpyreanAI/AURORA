DEFAULT_DIRS = ['up', 'down']

class BaseInsider(object):

    def __init__(self, id, stock, dirs=DEFAULT_DIRS):
        self.id = id
        self.stock = stock
        self.stock_wallet = []
        self.directions = dirs

    def add_stock(self, stock):
        self.stock_wallet.append(stock)

    def remove_stock(self):
        self.stock_wallet.pop(0)

    def get_stocks(self):
        return self.stock_wallet

    def get_stock_name(self):
        return self.stock

    def wallet_size(self):
        return len(self.stock_wallet)

    def notify(self):
        raise NotImplementedError("Insider must implement notify.")

    @classmethod
    def _log(cls, msg):
        raise NotImplementedError("Insider must implement log.")
