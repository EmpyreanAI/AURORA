import pymongo
import pprint
import datetime

class CRUD(object):

    def __init__(self):
        self.client = pymongo.MongoClient('127.0.0.1', 27017,
                                     username="Skalwalker",
                                     password="reka09")

        self.db = self.client.StockMarket

    def get_markets(self):
        d = datetime.datetime(2015, 3, 14)
        markets = self.db.Market.find({'_id': {'$gte': d}}).sort('_id')
        return markets

    def get_stock(self, date, stock):
        print(date)
        mkt = self.db.Market.find_one({'_id': date})
        stocks = mkt['stocks']
        print(type(stocks))

        return stock

if __name__ == '__main__':

    crud = CRUD()
    markets = crud.get_markets()
    market = markets[0]
    date = crud.get_stock(market['_id'], 'VALE3')
