import random
from .base import *

class RandomInsider(BaseInsider):

    def __init__(self, insider_id, stock, dirs=DEFAULT_DIRS):
        super(RandomInsider, self).__init__(insider_id, stock, dirs)
        self._log("Initialized")
        self._log("Stocks: {}".format(self.stock_wallet))

    def log_dir(self, dir):
        self._log("({0}): {1}".format(self.stock_name, dir))

    def predict_direction(self):
        dir_amount = len(self._directions)
        index = random.randrange(dir_amount)
        dir = self._directions[index]
        self.log_dir(dir)
        return dir

    def notify(self):
        return self.predict_direction()

    def _log(self, msg):
        print("[RandomInsider {}] {}".format(self.insider_id, msg))
