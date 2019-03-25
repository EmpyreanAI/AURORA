#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test Doc.

OWOWOW
"""
import math
import numpy as np
import pykka

from .crud import CRUD
from .plotter import Plotter

class StockMarket(pykka.ThreadingActor):

    def __init__(self, window_size, start_year, end_year):
        super(StockMarket, self).__init__()
        self._log("Initialized")
        self.window_size = window_size
        self.crud = CRUD()
        self.data = self._get_data(start_year, end_year)
        self.plotter = Plotter()

    def _get_data(self, start_year, end_year):
        data = self.crud.get_markets(start_year, end_year)
        return data

    def execute_buy(self, insider, stock):
        # insider.stock_wallet.append(stock)
        self._log("Stock being bought at {0:.2f}".format(stock['PREULT']))
        return stock

    def execute_sell(self, stock):
        # bought_price = insider.stock_wallet.pop(0)
        # bought_price = bought_price['PREULT']
        self._log("Stock being sold at {0:.2f}".format(stock['PREULT']))
        return stock['PREULT']

    def _get_state(self, time):
        window = time - self.window_size + 1
        # import pdb; pdb.set_trace()
        if window >= 0:
            block = self.data[window:time + 1]
        else:
            block = -window * [self.data[0]] + self.data[0:time + 1]

        return np.array([block[0:len(block)-1]])

    def on_receive(self, message):
        return 'DAY_PASSED'

    # def wait_for_actions(self):
        # return bool(self.brokerage._end_actions)

    def run(self):
        self._log("Running")
        bought = []
        sold = []
        for day in self.data:

            while self.wait_for_actions():
                pass
            # agent_money = self.agenst.cash
            # actions = self.agent.act(day['_id'], self.crud)

            # for insider, stock, action in actions:
                # if action == 'buy':
                    # self.execute_buy(insider, stock)
                    # bought.append((day['_id'], stock['PREULT']))
                # elif action == 'sell':
                    # self.execute_sell(insider, stock)
                    # sold.append((day['_id'], stock['PREULT']))


        # self.plotter.plot_one(self.data, bought, sold)

    @classmethod
    def _log(cls, msg):
        print("[StockMarket] {}".format(msg))

if __name__ == '__main__':
    try:
        MARKET = StockMarket()
        MARKET.RUN()
    except KeyboardInterrupt:
        print('\n\nInterrupted execution\n')
