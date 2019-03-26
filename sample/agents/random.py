import random
from agents.base import BaseAgent

class RandomAgent(BaseAgent):

    def __init__(self, agent_id, brokerage, actions, stocks, insider_type):
        self._log("Initialized")
        super(RandomAgent, self).__init__(agent_id, brokerage, actions,
                                          stocks, insider_type)
        self._log("Cash: {0:.2f}".format(self.cash))
        self._log("Profit: {0:.2f}".format(self.profit))


    def random_decider(self, stock_price, insider):
        if stock_price is not None:
            actions = self.actions[:]
            if self.cash < stock_price:
                actions.remove('buy')
            if insider.wallet_size() == 0:
                actions.remove('sell')
            if len(actions) == 0:
                actions.append('wait')
            actions_size = len(actions)
            index = random.randrange(actions_size)
            action = actions[index]
        else:
            action = 'wait'

        return action

    def act(self):
        infos = self.request_notifications()
        for insider, _ in infos:
            stock_name = insider.stock_name
            stock_price = self._brokerage.stock_price(stock_name)
            action = self.random_decider(stock_price, insider)
            self.log_action("{}: {}".format(stock_name, action))
            if action == 'buy':
                new_stock = self._brokerage.request_buy(self, stock_name, 1)
                insider.add_stock(new_stock)
            elif action == 'sell':
                self._brokerage.request_sell(self, stock_name, 1)
                insider.remove_stock()

    @classmethod
    def _log(cls, msg):
        print("[RandomAgent] {}".format(msg))

    def log_cash(self):
        self._log("Cash: {0:.2f}".format(self.cash))

    def log_profit(self):
        for insider in self.insiders:
            stocks = len(insider.stock_wallet)
            self.profit += stocks * self._brokerage.stock_price(insider.stock_name)
        self._log("Profit: {0:.2f}".format(self.profit+self.cash-1000))

    def log_action(self, act):
        act = act.capitalize() + "ing"
        self._log(act)
