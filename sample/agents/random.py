
import random
from agents.base import BaseAgent


class RandomAgent(BaseAgent):

    def __init__(self, actions):
        super(RandomAgent, self).__init__()
        self.actions = actions
        self.profit = 0
        self.stock_wallet = []
        self._log("Initialized")
        self._log("Cash: {0:.2f}".format(self.get_cash()))
        self._log("Stocks: {}".format(self.get_stocks()))
        self._log("Profit: {0:.2f}".format(self.get_profit()))

    def add_stock(self, stock):
        self.stock_wallet.append(stock)

    def remove_stock(self):
        self.stock_wallet.pop(0)

    def get_stocks(self):
        return self.stock_wallet

    def get_profit(self):
        return self.profit

    def log_cash(self):
        self._log("Cash: {0:.2f}".format(self.get_cash()))

    def log_action(self, act):
        act = act.capitalize()
        act = act + "ing"
        self._log(act)
        if act is 'sell' or 'buy':
            self.log_cash()

    def act(self, action_price):
        actions = self.actions.copy()
        if self.cash < action_price:
            actions.remove('buy')
        if len(self.stock_wallet) == 0:
            actions.remove('sell')
        actions_size = len(actions)
        index = random.randrange(actions_size)
        action = actions[index]
        self.log_action(action)
        return action

    @classmethod
    def _log(cls, msg):
        print("[RandomAgent] {}".format(msg))
