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
        d = datetime.datetime(1998, 3, 13)
        markets = self.db.Market.find({'_id': {'$gte': d}}).sort('_id')
        return markets

    def get_stock(self, date, stock):
        print(type(date))
        stock = self.db.Market.find_one({'_id': date}) #'stock': {'CODNEG': stock}
        for stock in stock['stocks']:
            print(stock['CODNEG'])

        return stock

if __name__ == '__main__':

    crud = CRUD()
    markets = crud.get_markets()
    market = markets[0]
    date = crud.get_stock(market['_id'], 'VAL 3')
