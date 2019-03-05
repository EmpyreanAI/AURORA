import pymongo
import pprint
import datetime
import sys

class CRUD(object):

    def __init__(self):
        self.client = pymongo.MongoClient('127.0.0.1', 27017,
                                     username="Skalwalker",
                                     password="reka09")

        self.db = self.client.StockMarket

    def _get_markets(self, start_year, end_year):
        s_d = datetime.datetime(start_year, 1, 1)
        e_d = datetime.datetime(end_year, 12, 31)
        markets = self.db.Market.find({'_id': {'$gte': s_d, '$lte': e_d}}).sort('_id')
        return markets

    def _get_stock(self, date, stock):
        mkt = self.db.Market.find_one({'_id': date,
                                       'stocks.CODNEG': stock},
                                      {'stocks.$': 1})
        try:
            stock = mkt['stocks'][0]
        except TypeError:
            stock = None

        return stock

if __name__ == '__main__':

    crud = CRUD()
    markets = crud.get_markets(1987, 2018)
    # for mkt in markets:
    #     stock = crud.get_stock(mkt['_id'], 'VALE3')
        # print(stock)
