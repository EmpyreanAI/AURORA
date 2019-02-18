import random
from insiders.base import *

class RandomInsider(BaseInsider):

    def __init__(self, id, stock, dirs=DEFAULT_DIRS):
        super(RandomInsider, self).__init__(id, stock, dirs)
        self._log("Initialized")
        self._log("Stocks: {}".format(self.get_stocks()))

    def log_dir(self, dir):
        self._log("({0}): {1}".format(self.stock, dir))

    def predict_direction(self):
        dir_amount = len(self.directions)
        index = random.randrange(dir_amount)
        dir = self.directions[index]
        self.log_dir(dir)
        return dir

    def notify(self):
        return self.predict_direction();

    def _log(self, msg):
        print("[RandomInsider {}] {}".format(self.id, msg))
