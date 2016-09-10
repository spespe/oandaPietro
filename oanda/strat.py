__author__ = 'Spe'

<<<<<<< HEAD
# required datetime functions
from datetime import datetime, timedelta
import data.access
import oandapy
import pandas as pd

class ForexSystem(oandapy.Streamer):
    def __init__(self, *args, **kwargs):
        oandapy.Streamer.__init__(self, *args, **kwargs)
        self.oanda = oandapy.API(kwargs["environment"], kwargs["access_token"])
        self.instrument = None
        self.account_id = None
        self.qty = 0
        self.resample_interval = '10s'
        self.mean_period_short = 5
        self.mean_period_long = 20
        self.buy_threshold = 1.0
        self.sell_threshold = 1.0
        self.prices = pd.DataFrame()
        self.beta = 0
        self.is_position_opened = False
        self.opening_price = 0
        self.executed_price = 0
        self.unrealized_pnl = 0
        self.realized_pnl = 0
        self.position = 0
        self.dt_format = "%Y-%m-%dT%H:%M:%S.%fZ"

def begin(self, **params):
    self.instrument = params["instruments"]
    self.account_id = params["accountId"]
    self.qty = params["qty"]
    self.resample_interval = params["resample_interval"]
    self.mean_period_short = params["mean_period_short"]
    self.mean_period_long = params["mean_period_long"]
    self.buy_threshold = params["buy_threshold"]
    self.sell_threshold = params["sell_threshold"]
    # Start streaming prices
    self.start(**params)

def on_success(self, data):
    time, symbol, bid, ask = self.parse_tick_data(data["tick"])
    self.tick_event(time, symbol, bid, ask)

def tick_event(self, time, symbol, bid, ask):
    midprice = (ask+bid)/2.
    self.prices.loc[time, symbol] = midprice
    resampled_prices = self.prices.resample(self.resample_interval, how='last', fill_method="ffill")
    mean_short = resampled_prices.tail(self.mean_period_short).mean()[0]
    mean_long = resampled_prices.tail(self.mean_period_long).mean()[0]
    self.beta = mean_short / mean_long
    self.perform_trade_logic(self.beta)
    self.calculate_unrealized_pnl(bid, ask)
    self.print_status()

def perform_trade_logic(self, beta):
    if beta > self.buy_threshold:
        if not self.is_position_opened or self.position < 0:
            self.check_and_send_order(True)
    elif beta < self.sell_threshold:
        if not self.is_position_opened or self.position > 0:
            self.check_and_send_order(False)

def print_status(self):
    print "[%s] %s pos=%s beta=%s RPnL=%s UPnL=%s" % (
        datetime.now().time(),
        self.instrument,
        self.position,
        round(self.beta, 5),
        self.realized_pnl,
        self.unrealized_pnl)
=======
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
>>>>>>> origin/master
