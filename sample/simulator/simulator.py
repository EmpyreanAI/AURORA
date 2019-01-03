#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test Doc.

OWOWOW
"""
import math
import numpy as np
from agents.random import RandomAgent
from simulator.plotter import Plotter
from simulator.inputdata import InputData

DEFAULT_STATE_SIZE = 10
DEFAULT_START_YEAR = 1993
DEFAULT_END_YEAR = 2018
DEFAULT_AGENT = 'random'
DEFAULT_STOCK = 'VALE3'
DEFAULT_ACTIONS = ['buy', 'sell', 'wait']


class Simulator(object):

    def __init__(self,
                 window_size=DEFAULT_STATE_SIZE,
                 actions=DEFAULT_ACTIONS,
                 stock=DEFAULT_STOCK,
                 agent=DEFAULT_AGENT,
                 start_year=DEFAULT_START_YEAR,
                 end_year=DEFAULT_END_YEAR):
        self._log("Initialized")
        self.window_size = window_size
        self.stock = stock
        self.sim_profit = 0
        self.actions = actions
        self.agent = self._register_agent(agent)
        self.data = self._get_data(start_year, end_year)
        self.data_len = len(self.data)-1
        self.plotter = Plotter()

    def _get_data(self, start_year, end_year):
        data = InputData(start_year, end_year)
        data_frame = data.stock_df(self.stock)
        data = np.array(data_frame[['PREULT']])
        data = np.reshape(data, len(data))
        data = data.tolist()
        return data

    def _register_agent(self, type):
        if type == 'random':
            return RandomAgent(self.actions)

    def _execute_buy(self, time):
        self.agent.sub_cash(self.data[time])
        self.agent.stock_wallet.append(self.data[time])
        self._log("Stock being bought at {0:.2f}".format(self.data[time]))

    def _execute_sell(self, time):
        bought_price = self.agent.stock_wallet.pop(0)
        self.sim_profit += self.data[time] - bought_price
        self.agent.add_cash(self.data[time])
        self._log("Stock being sold at {0:.2f}".format(self.data[time]))

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
        self.agent.add_cash(1000.00)
        self.agent.log_cash()
        bought = []
        sold = []
        for time in range(self.data_len):
            state = self._get_state(time)
            agent_money = self.agent.get_cash()
            action = self.agent.act(self.data[time])

            if action == 'buy':
                self._execute_buy(time)
                bought.append([self.data[time], time])
            elif action == 'sell':
                self._execute_sell(time)
                sold.append([self.data[time], time])

            reward = math.log((self.agent.get_cash()/agent_money), 10)

        self._log("Simulation Completed")
        self._log("Simulation profit: {0:.2f}".format(self.sim_profit))
        self.agent.log_cash()
        print(self.agent.stock_wallet)
        self.plotter.plot_one(self.data, bought, sold)

    @classmethod
    def _log(cls, msg):
        print("[Simulator] {}".format(msg))
