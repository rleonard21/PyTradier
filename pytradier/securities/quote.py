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

    def add_symbol(self, *symbols, **config):
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
        data = self._api_quote('symbol')

        return data

    def desc(self):
        data = self._api_quote('description')

        return data

    def exchange(self):
        data = self._api_quote('exch')

        return data

    def type(self):
        data = self._api_quote('type')

        return data

    def change(self):
        data = self._api_quote('change')

        return data

    def change_percentage(self):
        data = self._api_quote('change_percentage')

        return data

    def volume(self):
        data = self._api_quote('volume')

        return data

    def average_volume(self):
        data = self._api_quote('average_volume')

        return data

    def last_volume(self):
        data = self._api_quote('last_volume')

        return data

    def trade_date(self):
        data = self._api_quote('trade_date')

        return data

    def open(self):
        data = self._api_quote('open')

        return data

    def high(self):
        data = self._api_quote('high')

        return data

    def low(self):
        data = self._api_quote('low')

        return data

    def close(self):
        data = self._api_quote('close')

        return data

    def prevclose(self):
        data = self._api_quote('prevclose')

        return data

    def week_52_high(self):
        data = self._api_quote('week_52_high')

        return data

    def week_52_low(self):
        data = self._api_quote('week_52_low')

        return data

    def bid(self):
        data = self._api_quote('bid')

        return data

    def bidsize(self):
        data = self._api_quote('bidsize')

        return data

    def bidexch(self):
        data = self._api_quote('bidexch')

        return data

    def bid_date(self):
        data = self._api_quote('bid_date')

        return data

    def ask(self):
        data = self._api_quote('ask')

        return data

    def asksize(self):
        data = self._api_quote('asksize')

        return data

    def askexch(self):
        data = self._api_quote('askexch')

        return data

    def ask_date(self):
        data = self._api_quote('ask_date')

        return data
