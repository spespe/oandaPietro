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


trade_expire = datetime.utcnow() +timedelta(seconds=10)
trade_expire = trade_expire.isoformat("T") + "Z"

print(response)

response2 = oanda.create_order(data.access.account_id,
    instrument="EUR_USD",
    units=1,
    side='sell',
    type='limit',
    price=1.15,
    expiry=trade_expire
)
