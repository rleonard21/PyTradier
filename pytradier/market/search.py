from ..base import Base
from ..const import API_PATH

class Search(Base):

    def __init__(self, **query):
        Base.__init__(self)

        self._payload = {}

        if 'symbol' in query.keys():
            self._payload['q'] = query['symbol']

        if 'indexes' in query.keys():
            self._payload['indexes'] = query['type']

        self._path = API_PATH['search']
        self._data = self._api_response(endpoint=self._endpoint,
                                        path=self._path,
                                        payload=self._payload)

        self._key = self._data['securities']['security']
        self._inner_key = 'symbol'

    def symbol(self, **config):
        return self._parse_response(attribute='symbol', **config)

    def exchange(self, **config):
        return self._parse_response(attribute='exchange', **config)

    def type(self, **config):
        return self._parse_response(attribute='type', **config)

    def desc(self, **config):
        return self._parse_response(attribute='description', **config)



