import os
from ..base import Base
from ..const import API_PATH

class Quote(Base):
    '''Super class for quotes'''
    def __init__(self, *symbols):
        Base.__init__(self)

        self._endpoint = os.environ['API_ENDPOINT']
        self._symbols = []

        for symbol in symbols:
            self._symbols.append(symbol)

        self._symbol_load = ','.join(self._symbols)

        self._payload = {'symbols': self._symbol_load}

        self.__data = self._api_response(endpoint=self._endpoint,
                                      path=API_PATH['quotes'],
                                      payload=self._payload)

    def _api_quote(self, attribute):
        # returns the data from the API response in a dictionary for, {symbol0: data0, symbol1: data1, symbol2: data2}
        response_load = {}

        if len(self._symbols) is 1:
            # if there is only one symbol supplied, add it to the dictionary
            response_load[self.__data['quotes']['quote']['symbol']] = self.__data['quotes']['quote'][attribute]

        else:

            for quote in self.__data['quotes']['quote']:
                # more than one symbol supplied, loop through each one and add the strike price of each
                # option to the response_load dictionary

                response_load[quote['symbol']] = quote[attribute]

        return response_load

    def update_data(self):
        self.__data = self._api_response(endpoint=self._endpoint,
                                         path=API_PATH['quotes'],
                                         payload=self._payload)
        # print self.__data

    def add_symbols(self, *symbols, **config):
        # adds a given symbol to the array of tracked symbols. the `update` parameter chooses whether or not to
        # call the API for new data

        for symbol in symbols:  # iterate through each new symbol
            self._symbols.append(symbol)

        self._symbol_load = ','.join(self._symbols)
        self._payload = {'symbols': self._symbol_load}

        if 'update' in config.keys() and config['update'] is True:
            # update the data if the `update` parameter is true
            self.update_data()

    def symbol(self):
        return self._api_quote('symbol')

    def desc(self):
        return self._api_quote('description')

    def exchange(self):
        return self._api_quote('exch')

    def type(self):
        return self._api_quote('type')

    def change(self):
        return self._api_quote('change')

    def change_percentage(self):
        return self._api_quote('change_percentage')

    def volume(self):
        return self._api_quote('volume')

    def average_volume(self):
        return self._api_quote('average_volume')

    def last_volume(self):
        return self._api_quote('last_volume')

    def trade_date(self):
        return self._api_quote('trade_date')

    def open(self):
        return self._api_quote('open')

    def high(self):
        return self._api_quote('high')

    def low(self):
        return self._api_quote('low')

    def close(self):
        return self._api_quote('close')

    def prevclose(self):
        return self._api_quote('prevclose')

    def week_52_high(self):
        return self._api_quote('week_52_high')

    def week_52_low(self):
        return self._api_quote('week_52_low')

    def bid(self):
        return self._api_quote('bid')

    def bidsize(self):
        return self._api_quote('bidsize')

    def bidexch(self):
        return self._api_quote('bidexch')

    def bid_date(self):
        return self._api_quote('bid_date')

    def ask(self):
        return self._api_quote('ask')

    def asksize(self):
        return self._api_quote('asksize')

    def askexch(self):
        return self._api_quote('askexch')

    def ask_date(self):
        return self._api_quote('ask_date')
