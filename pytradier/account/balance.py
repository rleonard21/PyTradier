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
        if 'update' in config.keys() and config['update'] is False:
            pass

        else:
            # update the data if the `update` parameter is true
            self.update_data()  # updates by default, user must specify to not update from the API

        if 'inner' in config.keys():

            return self._data['balances'][attribute][config['inner']]

        else:
            return self._data['balances'][attribute]

    def account_number(self, **config):
        return self._parse_response(attribute='account_number', **config)

    def account_type(self, **config):
        return self._parse_response(attribute='account_type', **config)

    def cash_available(self, **config):
        return self._parse_response(attribute='cash', inner='cash_available',**config)

    def close_pl(self, **config):
        return self._parse_response(attribute='close_pl', **config)

    def current_requirement(self, **config):
        return self._parse_response(attribute='current_requirement', **config)

    def day_trade_buying_power(self, **config):
        return self._parse_response(attribute='day_trade_buying_power', **config)

    def dividend_balance(self, **config):
        return self._parse_response(attribute='dividend_balance', **config)

    def equity(self, **config):
        return self._parse_response(attribute='equity', **config)

    def fed_call(self, **config):
        return self._parse_response(attribute='fed_call', **config)

    def long_liquid_value(self, **config):
        return self._parse_response(attribute='long_liquid_value', **config)

    def long_market_value(self, **config):
        return self._parse_response(attribute='long_market_value', **config)

    def maintenance_call(self, **config):
        return self._parse_response(attribute='maintenance_call', **config)

    def market_value(self, **config):
        return self._parse_response(attribute='market_value', **config)

    def net_value(self, **config):
        return self._parse_response(attribute='net_value', **config)

    def open_pl(self, **config):
        return self._parse_response(attribute='open_pl', **config)

    def option_buying_power(self, **config):
        return self._parse_response(attribute='option_buying_power', **config)

    def option_long_value(self, **config):
        return self._parse_response(attribute='option_long_value', **config)

    def option_requirement(self, **config):
        return self._parse_response(attribute='option_requirement', **config)

    def option_short_value(self, **config):
        return self._parse_response(attribute='option_short_value', **config)

    def pending_cash(self, **config):
        return self._parse_response(attribute='pending_cash', **config)

    def pending_orders_count(self, **config):
        return self._parse_response(attribute='pending_orders_count', **config)

    def sweep(self, **config):
        return self._parse_response(attribute='cash', inner='sweep', **config)

    def short_liquid_value(self, **config):
        return self._parse_response(attribute='short_liquid_value', **config)

    def short_market_value(self, **config):
        return self._parse_response(attribute='short_market_value', **config)

    def stock_buying_power(self, **config):
        return self._parse_response(attribute='stock_buying_power', **config)

    def stock_long_value(self, **config):
        return self._parse_response(attribute='stock_long_value', **config)

    def stock_short_value(self, **config):
        return self._parse_response(attribute='stock_short_value', **config)

    def uncleared_funds(self, **config):
        return self._parse_response(attribute='uncleared_funds', **config)

    def unsettled_funds(self, **config):
        return self._parse_response(attribute='cash', inner='unsettled_funds', **config)

    def total_cash(self, **config):
        return self._parse_response(attribute='total_cash', **config)

    def total_equity(self, **config):
        return self._parse_response(attribute='total_equity', **config)




