from ..base import Base
from ..const import API_PATH
from ..const import API_ENDPOINT
import os
from ..exceptions import ClientException

class Balance(Base):
    def __init__(self):
        Base.__init__(self)

        if self._endpoint is not API_ENDPOINT['brokerage']:
            raise ClientException('Bad Endpoint: account paths require the full API (no sandbox!)')

        self._payload = {}
        self._path = API_PATH['account']
        self._path += os.environ['API_ACCOUNT_ID'] + '/balances'

        self._data = self._api_response(endpoint=self._endpoint,
                                        path=self._path,
                                        payload=self._payload)

        self._key = self._data['balances']


    def _parse_response(self, attribute, **config):
        # returns the data from the API response in a dictionary for, {symbol0: data0, symbol1: data1, symbol2: data2}
        # overrides from Base super since response must be a dictionary

        if 'update' in config.keys() and config['update'] is False:
            # update the data if the `update` parameter is true
            pass

        else:
            self.update_data()  # updates by default, user must specify to not update from the API

        return self._data['balances'][attribute]


    def account_number(self, **config):
        return self._parse_response(attribute='account_number', **config)

    def account_type(self, **config):
        return self._parse_response(attribute='account_number', **config)

    def cash_available(self, **config):
        return self._parse_response(attribute='account_number', **config)

    def close_pl(self, **config):
        return self._parse_response(attribute='account_number', **config)

    def current_requirement(self, **config):
        return self._parse_response(attribute='account_number', **config)

    def day_trade_buying_power(self, **config):
        return self._parse_response(attribute='account_number', **config)

    def dividend_balance(self, **config):
        return self._parse_response(attribute='account_number', **config)

    def equity(self, **config):
        return self._parse_response(attribute='account_number', **config)

    def fed_call(self, **config):
        return self._parse_response(attribute='account_number', **config)

    def long_liquid_value(self, **config):
        return self._parse_response(attribute='account_number', **config)

    def long_market_value(self, **config):
        return self._parse_response(attribute='account_number', **config)

    def maintenance_call(self, **config):
        return self._parse_response(attribute='account_number', **config)

    def market_value(self, **config):
        return self._parse_response(attribute='account_number', **config)

    def net_value(self, **config):
        return self._parse_response(attribute='account_number', **config)

    def open_pl(self, **config):
        return self._parse_response(attribute='account_number', **config)

    def option_buying_power(self, **config):
        return self._parse_response(attribute='account_number', **config)

    def option_long_value(self, **config):
        return self._parse_response(attribute='account_number', **config)

    def option_requirement(self, **config):
        return self._parse_response(attribute='account_number', **config)

    def option_short_value(self, **config):
        return self._parse_response(attribute='account_number', **config)

    def pending_cash(self, **config):
        return self._parse_response(attribute='account_number', **config)

    def pending_orders_count(self, **config):
        return self._parse_response(attribute='account_number', **config)

    def sweep(self, **config):
        return self._parse_response(attribute='account_number', **config)

    def short_liquid_value(self, **config):
        return self._parse_response(attribute='account_number', **config)

    def short_market_value(self, **config):
        return self._parse_response(attribute='account_number', **config)

    def stock_buying_power(self, **config):
        return self._parse_response(attribute='account_number', **config)

    def stock_long_value(self, **config):
        return self._parse_response(attribute='account_number', **config)

    def stock_short_value(self, **config):
        return self._parse_response(attribute='account_number', **config)

    def uncleared_funds(self, **config):
        return self._parse_response(attribute='account_number', **config)

    def unsettled_funds(self, **config):
        return self._parse_response(attribute='account_number', **config)

    def total_cash(self, **config):
        return self._parse_response(attribute='account_number', **config)

    def total_equity(self, **config):
        return self._parse_response(attribute='account_number', **config)




