
class BaseAgent(object):

    def __init__(self):
        self.cash = 0

    def zero_cash(self):
        self.cash = 0

    def add_cash(self, cash):
        self.cash = self.cash + cash

    def sub_cash(self, cash):
        self.cash = self.cash - cash

    def get_cash(self):
        return self.cash

    def act(self):
        raise NotImplementedError("Agent must implement act.")

    @classmethod
    def _log(cls, msg):
        raise NotImplementedError("Agent must implement log.")
