from ..const import API_PATH

from ..base import Base

class Calendar(Base):
    def __init__(self, month=None, year=None):
        Base.__init__(self)

        self._payload = {}

        if month is not None:
            self._payload['month'] = month

        if year is not None:
            self._payload['year'] = year

        self._path = API_PATH['calendar']
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

        for response in self._data['calendar']['days']['day']:
            # more than one symbol supplied, loop through each one
            if attribute in response.keys():
                response_load[response['date']] = response[attribute]

            else:
                # this ensures that days when market is closed return None type if a market attribute is called.
                response_load[response['date']] = None

        return response_load


    def month(self, **config):
        return self._data['calendar']['month']

    def year(self, **config):
        return self._data['calendar']['year']

    def date(self, **config):
        return self._parse_response(attribute='date', **config)

    def status(self, **config):
        return self._parse_response(attribute='status', **config)

    def desc(self, **config):
        return self._parse_response(attribute='description', **config)

    def premarket(self, **config):
        return self._parse_response(attribute='premarket', **config)

    def open(self, **config):
        return self._parse_response(attribute='open', **config)

    def postmarket(self, **config):
        return self._parse_response(attribute='postmarket', **config)

    def start(self, **config):
        pass  # return self._parse_response(attribute='start', **config)

    def end(self, **config):
        pass  #return self._parse_response(attribute='end', **config)