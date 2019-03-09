#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test Doc.

OWOWOW
"""
import math
import numpy as np

from .crud import CRUD
from .plotter import Plotter
from agents.random import RandomAgent


class StockMarket(object):

    def __init__(self, agent, window_size, start_year, end_year):
        self._log("Initialized")
        self.window_size = window_size
        self.agent = agent
        self.crud = CRUD()
        self.data = self._get_data(start_year, end_year)
        self.plotter = Plotter()

    def _get_data(self, start_year, end_year):
        data = self.crud._get_markets(start_year, end_year)
        return data

    def _execute_buy(self, insider, stock):
        self.agent.cash_sub(stock['PREULT'])
        insider.stock_wallet.append(stock)
        self._log("Stock being bought at {0:.2f}".format(stock['PREULT']))

    def _execute_sell(self, insider, stock):
        bought_price = insider.stock_wallet.pop(0)
        bought_price = bought_price['PREULT']
        self.agent.profit_add(stock['PREULT'] - bought_price)
        self.agent.cash_add(stock['PREULT'])
        self._log("Stock being sold at {0:.2f}".format(stock['PREULT']))

    def _get_state(self, time):
        window = time - self.window_size + 1
        # import pdb; pdb.set_trace()
        if window >= 0:
            block = self.data[window:time + 1]
        else:
            block = -window * [self.data[0]] + self.data[0:time + 1]

        return np.array([block[0:len(block)-1]])

    def _format_price(n):
        return ("-$" if n < 0 else "$") + "{0:.2f}".format(abs(n))

    def run(self):
        self._log("Running")
        self.agent.cash_add(1000.00)
        self.agent.log_cash()
        bought = []
        sold = []
        for day in self.data:
            # state = self._get_state(time)
            agent_money = self.agent.cash
            actions = self.agent.act(day['_id'], self.crud)

            for insider, stock, action in actions:
                if action == 'buy':
                    self._execute_buy(insider, stock)
                    bought.append((day['_id'], stock['PREULT']))
                elif action == 'sell':
                    self._execute_sell(insider, stock)
                    sold.append((day['_id'], stock['PREULT']))
            reward = math.log((self.agent.cash/agent_money), 10)

        self._log("Simulation Completed")
        self._log("Simulation profit: {0:.2f}".format(self.agent.profit))
        self.agent.log_cash()
        # self.plotter.plot_one(self.data, bought, sold)

    @classmethod
    def _log(cls, msg):
        print("[StockMarket] {}".format(msg))
