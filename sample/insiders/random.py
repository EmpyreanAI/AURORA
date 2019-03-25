import random
from .base import BaseInsider, DEFAULT_DIRS

class RandomInsider(BaseInsider):

    def __init__(self, insider_id, stock, dirs=DEFAULT_DIRS):
        super(RandomInsider, self).__init__(insider_id, stock, dirs)
        self._log("Initialized")
        self._log("Stocks: {}".format(self.stock_wallet))

    def predict_direction(self):
        dir_amount = len(self._directions)
        index = random.randrange(dir_amount)
        directions = self._directions[index]
        self.log_direction(directions)
        return directions

    def notify(self):
        return self.predict_direction()

    def log_direction(self, direction):
        self._log("({0}): {1}".format(self.stock_name, direction))

    def _log(self, msg):
        print("[RandomInsider {}] {}".format(self.insider_id, msg))
