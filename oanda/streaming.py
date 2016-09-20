__author__ = 'Spe'

import oandapy
import data.access
import requests

class streaming:
    """This class is created to stream prices from oanda in realtime"""
    def __init__(self, instruments):
        self.domain = data.access.domain
        self.key = data.access.key
        self.account_id = data.access.account_id
        self.instruments = instruments

    def connect(self):
        try:
            session = requests.Session()
            url = "https://" + self.domain + "/v1/prices"
            headers = {'Authorization': 'Bearer ' + self.key}
            params = {'instruments': self.instruments, 'accountId': self.account_id}
            req = requests.Request('GET', url, headers=headers, params=params)
            pre = req.prepare()
            resp = session.send(pre, stream=True, verify=False)
            return resp
        except Exception as ex:
            print("Exception found while connecting to oanda. "+str(ex))
            self.session.close()

