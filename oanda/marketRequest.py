__author__ = 'Spe'


import json
import requests
import exceptions

class action:
    """This class will contain all the methods commonly used to enter or exit from the market.
    It also contains methods created to return the status of the positions opened in the market."""

    def request(self, endpoint, method='GET', params=None):
            """Returns dict of response from OANDA's open API
            :param endpoint: (required) OANDA API (e.g. v1/instruments)
            :type endpoint: string
            :param method: (optional) Method of accessing data, either GET or POST.
             (default GET)
            :type method: string
            :param params: (optional) Dict of parameters (if any) accepted the by
             OANDA API endpoint you are trying to access (default None)
            :type params: dict or None
            """

            url = '%s/%s' % (self.api_url, endpoint)

            method = method.lower()
            params = params or {}

            func = getattr(self.client, method)

            request_args = {}
            if method == 'get':
                request_args['params'] = params
            else:
                request_args['data'] = params

            try:
                response = func(url, **request_args)
            except requests.RequestException as e:
                print (str(e))
            content = response.content.decode('utf-8')

            content = json.loads(content)

            # error message
            if response.status_code >= 400:
                raise exceptions.OandaError(content)

            return content

    def get_instruments(self, account_id, **params):
        params['accountId'] = account_id
        endpoint = 'v1/instruments'
        return self.request(endpoint, params=params)

    def get_prices(self, **params):
        endpoint = 'v1/prices'
        return self.request(endpoint, params=params)

    def get_history(self, **params):
        endpoint = 'v1/candles'
        return self.request(endpoint, params=params)

    def get_orders(self, account_id, **params):
        endpoint = 'v1/accounts/%s/orders' % (account_id)
        return self.request(endpoint, params=params)

    def create_order(self, account_id, **params):
        endpoint = 'v1/accounts/%s/orders' % (account_id)
        return self.request(endpoint, "POST", params=params)

    def get_order(self, account_id, order_id, **params):
        endpoint = 'v1/accounts/%s/orders/%s' % (account_id, order_id)
        return self.request(endpoint, params=params)

    def modify_order(self, account_id, order_id, **params):
        endpoint = 'v1/accounts/%s/orders/%s' % (account_id, order_id)
        return self.request(endpoint, "PATCH", params=params)

    def close_order(self, account_id, order_id, **params):
        endpoint = 'v1/accounts/%s/orders/%s' % (account_id, order_id)
        return self.request(endpoint, "DELETE", params=params)

    def get_trades(self, account_id, **params):
        endpoint = 'v1/accounts/%s/trades' % (account_id)
        return self.request(endpoint, params=params)

    def get_trade(self, account_id, trade_id, **params):
        endpoint = 'v1/accounts/%s/trades/%s' % (account_id, trade_id)
        return self.request(endpoint, params=params)

    def modify_trade(self, account_id, trade_id, **params):
        endpoint = 'v1/accounts/%s/trades/%s' % (account_id, trade_id)
        return self.request(endpoint, "PATCH", params=params)

    def close_trade(self, account_id, trade_id, **params):
        endpoint = 'v1/accounts/%s/trades/%s' % (account_id, trade_id)
        return self.request(endpoint, "DELETE", params=params)

    def get_positions(self, account_id, **params):
        endpoint = 'v1/accounts/%s/positions' % (account_id)
        return self.request(endpoint, params=params)

    def get_position(self, account_id, instrument, **params):
        endpoint = 'v1/accounts/%s/positions/%s' % (account_id, instrument)
        return self.request(endpoint, params=params)

    def close_position(self, account_id, instrument, **params):
        endpoint = 'v1/accounts/%s/positions/%s' % (account_id, instrument)
        return self.request(endpoint, "DELETE", params=params)

    def get_transaction_history(self, account_id, **params):
        endpoint = 'v1/accounts/%s/transactions' % (account_id)
        return self.request(endpoint, params=params)

    def get_transaction(self, account_id, transaction_id):
        endpoint = 'v1/accounts/%s/transactions/%s' % \
                   (account_id, transaction_id)
        return self.request(endpoint)
