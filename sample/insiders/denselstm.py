from keras.models import load_model
from .base import BaseInsider, DEFAULT_DIRS

class DenseLSTMInsider(BaseInsider):

    def __init__(self, insider_id, stock, dirs=DEFAULT_DIRS):
        super(DenseLSTMInsider, self).__init__(insider_id, stock, dirs)
        self._log("Initialized")
        self._log("Stocks: {}".format(self.stock_wallet))
        self.model = load_model('VALE3-model.h5')

    def predict_direction(self):
        model = load_model('denselstm.h5')
        return

    def notify(self):
        return self.predict_direction()

    def log_direction(self, direction):
        self._log("({0}): {1}".format(self.stock_name, direction))

    def _log(self, msg):
        print("[LSTMInsider {}] {}".format(self.insider_id, msg))
