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




        print self._payload

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
            print response

            # more than one symbol supplied, loop through each one
            if attribute in response.keys():
                response_load[response['date']] = response[attribute]

            else:
                # this ensures that days when market is closed return None type if a market attribute is called.
                response_load[response['date']] = None

        return response_load






    def symbol(self):
        pass

    def exchange(self):
        pass

    def type(self):
        pass

    def desc(self):
        pass