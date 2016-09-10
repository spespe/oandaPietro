__author__ = 'Spe'

import oandapy, pyoanda, quintoandar_eb_deployer
import data.access


oanda = oandapy.API(environment="practice", access_token=data.access.key)
response = oanda.get_prices(instruments="EUR_USD")


prices = response["prices"]
bidding_price = float(prices[0]["bid"])
asking_price = float(prices[0]["ask"])
instrument = prices[0]["instrument"]
time = prices[0]["time"]


print "[%s] %s bid=%s ask=%s" % (time, instrument, bidding_price, asking_price)
