from ..base import Base
from ..const import API_PATH

class Quote(Base):
    '''Super class for quotes'''
    def __init__(self, *symbols):
        Base.__init__(self)

        self._symbols = []

        for symbol in symbols:
            self._symbols.append(symbol)

        self._symbol_load = ','.join(self._symbols)

        self._path = API_PATH['quotes']
        self._payload = {'symbols': self._symbol_load}
        self._data = self._api_response(endpoint=self._endpoint,
                                      path=self._path,
                                      payload=self._payload)


    def _api_quote(self, attribute, **config):
        # returns the data from the API response in a dictionary for, {symbol0: data0, symbol1: data1, symbol2: data2}

        if 'update' in config.keys() and config['update'] is False:
            # update the data if the `update` parameter is true
            print 'not updating'
            pass

        else:
            print 'updating'
            self.update_data()  # updates by default, user must specify to not update from the API


        response_load = {}

        if len(self._symbols) is 1:
            # if there is only one symbol supplied, add it to the dictionary
            response_load[self._data['quotes']['quote']['symbol']] = self._data['quotes']['quote'][attribute]

        else:

            for quote in self._data['quotes']['quote']:
                # more than one symbol supplied, loop through each one

                response_load[quote['symbol']] = quote[attribute]

        return response_load

    def add_symbols(self, *symbols, **config):
        # adds a given symbol to the array of tracked symbols. the `update` parameter chooses whether or not to
        # call the API for new data

        for symbol in symbols:  # iterate through each new symbol
            self._symbols.append(symbol)

        self._symbol_load = ','.join(self._symbols)  # change form from array to CSV: [AAPL, MSFT] -> AAPL,MSFT
        self._payload = {'symbols': self._symbol_load}  # prepare the payload

        if 'update' in config.keys() and config['update'] is False:
            # update the data if the `update` parameter is true
            pass

        else:
            self.update_data()  # updates by default, user must specify to not update from the API

    def symbol(self, **config):
        return self._api_quote(attribute='symbol', **config)  # pass the desired variable in with the settings, if used

    def desc(self, **config):
        return self._api_quote(attribute='description', **config)

    def exchange(self, **config):
        return self._api_quote(attribute='exch', **config)

    def type(self, **config):
        return self._api_quote(attribute='type', **config)

    def change(self, **config):
        return self._api_quote(attribute='change', **config)

    def change_percentage(self, **config):
        return self._api_quote(attribute='change_percentage', **config)

    def volume(self, **config):
        return self._api_quote(attribute='volume', **config)

    def average_volume(self, **config):
        return self._api_quote(attribute='average_volume', **config)

    def last_volume(self, **config):
        return self._api_quote(attribute='last_volume', **config)

    def trade_date(self, **config):
        return self._api_quote(attribute='trade_date', **config)

    def open(self, **config):
        return self._api_quote(attribute='open', **config)

    def high(self, **config):
        return self._api_quote(attribute='high', **config)

    def low(self, **config):
        return self._api_quote(attribute='low', **config)

    def close(self, **config):
        return self._api_quote(attribute='close', **config)

    def prevclose(self, **config):
        return self._api_quote(attribute='prevclose', **config)

    def week_52_high(self, **config):
        return self._api_quote(attribute='week_52_high', **config)

    def week_52_low(self, **config):
        return self._api_quote(attribute='week_52_low', **config)

    def bid(self, **config):
        return self._api_quote(attribute='bid', **config)

    def bidsize(self, **config):
        return self._api_quote(attribute='bidsize', **config)

    def bidexch(self, **config):
        return self._api_quote(attribute='bidexch', **config)

    def bid_date(self, **config):
        return self._api_quote(attribute='bid_date', **config)

    def ask(self, **config):
        return self._api_quote(attribute='ask', **config)

    def asksize(self, **config):
        return self._api_quote(attribute='asksize', **config)

    def askexch(self, **config):
        return self._api_quote(attribute='askexch', **config)

    def ask_date(self, **config):
        return self._api_quote(attribute='ask_date', **config)
