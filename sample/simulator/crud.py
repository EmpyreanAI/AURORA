import datetime
import pymongo


class CRUD():

    def __init__(self):
        self.client = pymongo.MongoClient()

        self.db = self.client.StockMarket

    def get_markets(self, start_year, end_year):
        s_d = datetime.datetime(start_year, 1, 1)
        e_d = datetime.datetime(end_year, 12, 31)
        markets = self.db.Market.find({'_id': {'$gte': s_d,
                                               '$lte': e_d}}).sort('_id')
        return markets

    def get_stock(self, date, stock):
        mkt = self.db.Market.find_one({'_id': date,
                                       'stocks.CODNEG': stock},
                                      {'stocks.$': 1})
        try:
            stock = mkt['stocks'][0]
        except TypeError:
            stock = None

        return stock
