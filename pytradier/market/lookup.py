from ..base import Base
from ..const import API_PATH

class Lookup(Base):
    def __init__(self, **query):
        Base.__init__(self)

        self._payload = {}

        if 'symbol' in query.keys():
            self._payload['q'] = query['symbol']

        if 'type' in query.keys():
            self._payload['type'] = query['type']

        if 'exchange' in query.keys():
            self._payload['exchanges'] = query['exchange']

        self._path = API_PATH['lookup']
        self._data = self._api_response(endpoint=self._endpoint,
                                        path=self._path,
                                        payload=self._payload)

    def _parse_response(self, attribute, **config):
        # returns the data from the API response in a dictionary for, {symbol0: data0, symbol1: data1, symbol2: data2}
        # overrides from Base super since response must be a dictionary

        if 'update' in config.keys() and config['update'] is False:
            # update the data if the `update` parameter is true
            pass

        else:
            self.update_data()  # updates by default, user must specify to not update from the API


        response_load = {}

        for response in self._data['securities']['security']:
            # more than one symbol in response, loop through each one

            response_load[response['symbol']] = response[attribute]

        return response_load

    def symbol(self, **config):
        return self._parse_response(attribute='symbol', **config)

    def exchange(self, **config):
        return self._parse_response(attribute='exchange', **config)

    def type(self, **config):
        return self._parse_response(attribute='type', **config)

    def desc(self, **config):
        return self._parse_response(attribute='description', **config)