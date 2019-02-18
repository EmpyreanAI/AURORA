import pymongo

class CRUD(object):

    def __init__(self):
        self.client = pymongo.MongoClient('127.0.0.1', 27017,
                                     username="Skalwalker",
                                     password="reka09")

        self.db = self.client.StockMarket

    def get_market(self):
        markets = self.db.Market.find({}).sort('_id')
        for market in markets:
            print(market['_id'])


if __name__ == '__main__':

    crud = CRUD()
    crud.get_market()
