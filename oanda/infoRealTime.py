__author__ = 'Spe'

import oandapy
import data.access

class CurrentPrice:
    """Class created to obtain information on the current prices"""
    def __init__(self, response):
        self.response = self.get_response()
        self.prices = response["prices"]
        self.ask_price = self.get_ask_price()
        self.bid_price = self.get_bid_price()
        self.spread = self.get_spread()
        self.instrument = self.get_instrument()
        self.time = self.get_time()

    def get_response(self):
        return response

    def get_bid_price(self):
        bid_price = float(self.prices[0]["bid"])
        return bid_price

    def get_ask_price(self):
        ask_price = float(self.prices[0]["ask"])
        return ask_price

    def get_spread(self):
        spread = self.get_ask_price() - self.get_bid_price()
        return spread

    def get_instrument(self):
        instrument = self.prices[0]["instrument"]
        return instrument

    def get_time(self):
        time = self.prices[0]["time"]
        return time


oanda = oandapy.API(environment="practice", access_token=data.access.key)
response = oanda.get_prices(instruments="EUR_USD")
current = CurrentPrice(response)

print(current.response)
print(current.bid_price)
print(current.ask_price)
print(current.spread)
print(current.instrument)
print(current.time)
