from .stock import Stock

class Brokerage():

    def __init__(self, market, fee):
        self._agent = None
        self.day = None
        self._fee = fee
        self.market = market


    @property
    def agent(self):
        return self._agent

    def stock_info(self, stock):
        return self.market.get_stock_info(self.day, stock)

    def stock_price(self, stock_name):
        stock = self.stock_info(stock_name)
        if stock is not None:
            stock_price = stock['PREULT']
        else:
            stock_price = None
        return stock_price

    def request_actions(self):
        self.agent.act()

    def register_agent(self, agent):
        self._agent = agent

    def request_buy(self, agent, stock_name, ammount):
        stock = self.stock_info(stock_name)
        bought_stock = self.market.execute_buy(stock)
        stock_price = self.stock_price(stock_name)
        agent.cash_sub(stock_price)
        return Stock(stock_name, stock_price, self.day)
        # da o stock comprado para o agent

    def request_sell(self, agent, stock_name, ammount):
        stock = self.stock_info(stock_name)
        cash = self.market.execute_sell(stock)
        agent.cash_add(cash - self._fee)

    def run(self):
        for day in self.market.run():
            self.day = day['_id']
            self.request_actions()
