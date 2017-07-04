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


    def symbol(self):
        return self._parse_response(attribute='symbol', update=False)

    def strike(self):
        return self._parse_response(attribute='strike', update=False)

    def last(self):
        return self._parse_response(attribute='last', update=False)

    def bid(self):
        return self._parse_response(attribute='bid', update=False)

    def ask(self):
        return self._parse_response(attribute='ask', update=False)

    def change(self):
        return self._parse_response(attribute='change', update=False)

    def interest(self):
        return self._parse_response(attribute='open_interest', update=False)