__author__ = 'Spe'

import oandapy
import data.access
import requests
import json
import urllib2

class streaming:
    """This class is created to stream prices from oanda in realtime"""
    def __init__(self, instruments):
        self.domain = data.access.domain_stream
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
            resp = requests.Session.send(session, pre, stream=True, verify=False)
            return resp
        except Exception as ex:
            print("Exception found while connecting to oanda. "+str(ex))
            session.close()


stream = streaming("EUR_USD")
stream.connect()

#if stream.connect().status_code != 200:
#    print stream.connect().text
#    for line in stream.connect().iter_lines(1):
#        if line:
#            try:
#                msg = json.loads(line)
#            except Exception as e:
#                print "Caught exception when converting message into json\n" + str(e)
#            print line

