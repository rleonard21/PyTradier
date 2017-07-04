from ..base import Base
from ..const import API_PATH

class Chain(Base):

    def __init__(self, symbol, expiration):
        Base.__init__(self)

        self._symbol = symbol
        self._expiration = expiration



        self._payload = {'symbol': self._symbol,
                         'expiration': self._expiration}

        self._path = API_PATH['chains']
        self._data = self._api_response(endpoint=self._endpoint,
                                        path=self._path,
                                        payload=self._payload)

        self._key = self._data['options']['option']
        self._inner_key = 'symbol'


    def symbol(self, **config):
        return self._parse_response(attribute='symbol', **config)

    def strike(self, **config):
        return self._parse_response(attribute='strike', **config)

    def last(self, **config):
        return self._parse_response(attribute='last', **config)

    def bid(self, **config):
        return self._parse_response(attribute='bid', **config)

    def ask(self, **config):
        return self._parse_response(attribute='ask', **config)

    def change(self, **config):
        return self._parse_response(attribute='change', **config)

    def interest(self, **config):
        return self._parse_response(attribute='open_interest', **config)