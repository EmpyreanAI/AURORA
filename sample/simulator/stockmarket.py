#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test Doc.

OWOWOW
"""
import math
import numpy as np

from .crud import CRUD
from .plotter import Plotter

class StockMarket(object):

    def __init__(self, window_size, start_year, end_year):
        self._log("Initialized")
        self.window_size = window_size
        self.crud = CRUD()
        self.data = self._get_data(start_year, end_year)
        self.plotter = Plotter()

    def _get_data(self, start_year, end_year):
        data = self.crud.get_markets(start_year, end_year)
        return data

    def get_stock_info(self, day, stock):
        return self.crud.get_stock(day, stock)

    def execute_buy(self, stock):
        self._log("Stock being bought at {0:.2f}".format(stock['PREULT']))
        return stock

    def execute_sell(self, stock):
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

    def run(self):
        self._log("Running")
        for day in self.data:
            yield day

    @classmethod
    def _log(cls, msg):
        print("[StockMarket] {}".format(msg))
