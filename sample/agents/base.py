from insiders.random import RandomInsider

class BaseAgent(object):

    def __init__(self, actions, stocks):
        self.cash = 0
        self.profit = 0
        self.actions = self._select_actions(actions)
        insider_id = 0
        self.insiders = []
        for stock in stocks:
            self.insiders.append(self._register_insider(insider_id, "random", stock))
            insider_id += 1

    def zero_cash(self):
        self.cash = 0

    def add_cash(self, cash):
        self.cash = self.cash + cash

    def sub_cash(self, cash):
        self.cash = self.cash - cash

    def get_cash(self):
        return self.cash

    def log_cash(self):
        self._log(self.cash)

    def add_profit(self, profit):
        self.profit = self.profit + profit

    def zero_profit(self):
        self.profit = 0

    def get_profit(self):
        return self.profit

    def request_notifications(self):
        notifications = []
        for insider in self.insiders:
            notifications.append((insider, insider.notify()))
        return notifications


    def _select_actions(self, actions):
        if actions == 'all':
            return ['buy', 'sell', 'wait']
        elif actions == 'nowait':
            return ['buy', 'sell']
        else:
            raise ValueError("Action must be 'all' or 'nowait'.")

    def _register_insider(self, id, type, stock):
        if type == 'random':
            return RandomInsider(id, stock)
        else:
            raise ValueError("Insider must be 'random'.")

    def act(self):
        raise NotImplementedError("Agent must implement act.")

    @classmethod
    def _log(cls, msg):
        raise NotImplementedError("Agent must implement log.")
