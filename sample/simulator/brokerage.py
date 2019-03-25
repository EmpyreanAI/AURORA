
import pykka

class Brokerage(pykka.ThreadingActor):

    def __init__(self, market, fee):
        super(Brokerage, self).__init__()
        self._agents = []
        self._fee = fee
        self.market = market
        self._end_actions = False

    @property
    def agents(self):
        return self._agents

    @property
    def end_actions(self):
        return self._end_actions

    @end_actions.setter
    def end_actions(self):
        self._end_actions = True

    def register_agent(self, agent_name):
        self._agents.append(agent_name)

    def request_buy(self, agent, stock, ammount):
        bought_stock = self.market.execute_buy()
        agent.cash_sub(stock['PREULT'])
        # da o stock comprado para o agent

    def request_sell(self, agent, stock, ammount):
        cash = self.market.execute_sell()
        agent.cash_add(cash - self._fee)

    def please_pass_the_day(self):
        response = self.market.ask({"msg": "PASS_DAY"})
        print(response)
