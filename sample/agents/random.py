import random
from agents.base import BaseAgent

class RandomAgent(BaseAgent):

    def __init__(self, agent_id, brokerage, actions, stocks, insider_type):
        self._log("Initialized")
        super(RandomAgent, self).__init__(agent_id, brokerage, actions,
                                          stocks, insider_type)
        self._log("Cash: {0:.2f}".format(self.cash))
        self._log("Profit: {0:.2f}".format(self.profit))

    def act(self, day, crud):
        infos = self.request_notifications()
        selected_actions = []
        temp_cash = self.cash
        for insider, info in infos:
            stock_name = insider.stock_name
            stock = crud.get_stock(day, stock_name)
            if stock is not None:
                stock_price = stock['PREULT']
                actions = self.actions[:]
                if temp_cash < stock_price:
                    actions.remove('buy')
                if insider.wallet_size() == 0:
                    actions.remove('sell')
                actions_size = len(actions)
                index = random.randrange(actions_size)
                action = actions[index]
                if action == 'buy':
                    temp_cash -= stock_price
            else:
                action = 'wait'
            self.log_action("{}: {}".format(stock_name, action))
            selected_actions.append((insider, stock, action))
        return selected_actions

    @classmethod
    def _log(cls, msg):
        print("[RandomAgent] {}".format(msg))

    def log_cash(self):
        self._log("Cash: {0:.2f}".format(self.cash))

    def log_profit(self):
        self._log("Profit: {0:.2f}".format(self.profit))

    def log_action(self, act):
        act = act.capitalize() + "ing"
        self._log(act)
