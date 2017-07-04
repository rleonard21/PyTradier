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
            print response

        print response_load


