__author__ = 'Spe'

from datetime import datetime, timedelta
import oanda.data.access
import oandapy
import pandas as pd


class PietroSystem(oandapy.Streamer):
    def __init__(self, *args, **kwargs):
        oandapy.Streamer.__init__(self, *args, **kwargs)
        self.access = oandapy.API(kwargs["environment"], kwargs["access_token"])
        self.instrument = None
        self.account_id = None
        self.qty = 0
        self.resample_interval = '10s'
        self.mean_period_short = 5
        self.mean_period_long = 20
        self.buy_threshold = 1.0
        self.sell_threshold = 1.0
        self.prices = pd.DataFrame()
        self.stop_loss = 40
        self.trailing_stop = 40
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

    #Need to override the on_success
    #def on_success(self, data):
    #    time, symbol, bid, ask = self.parse_tick_data(data["tick"])
    #    self.tick_event(time, symbol, bid, ask)

    def tick_event(self, time, symbol, bid, ask):
        midprice = (ask+bid)/2.
        self.prices.loc[time, symbol] = midprice
        resampled_prices = self.prices.resample(self.resample_interval, how='last', fill_method="ffill")
        mean_short = resampled_prices.tail(self.mean_period_short).mean()[0]
        mean_long = resampled_prices.tail(self.mean_period_long).mean()[0]
        self.beta = mean_short / mean_long
        self.perform_trade_logic(self.beta)
        self.print_status()

    def perform_trade_logic(self, beta):
        if beta > self.buy_threshold:
            if not self.is_position_opened or self.position < 0:
                #Adding check_and send_order method
                #self.check_and_send_order(True)
                print("check and sent order")
        elif beta < self.sell_threshold:
            if not self.is_position_opened or self.position > 0:
                #Adding check_and send_order method
                #self.check_and_send_order(False)
                print("check and sent order")

    def print_status(self):
        print "[%s] %s pos=%s beta=%s RPnL=%s UPnL=%s" % (
            datetime.now().time(),
            self.instrument,
            self.position,
            round(self.beta, 5),
            self.realized_pnl,
            self.unrealized_pnl)





#Change the main to include new changes
if __name__ == "__main__":
    system = PietroSystem(environment="practice", access_token=oanda.data.access.key)
    system.begin(accountId=oanda.data.access.account_id, instruments="EUR_USD", qty=1000, resample_interval="10s",
                 mean_period_short=5, mean_period_long=20, buy_threshold=1., sell_threshold=1.)


