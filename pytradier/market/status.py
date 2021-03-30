from ..base import Base
from ..const import API_PATH

import time


class Status(Base):
    """ A class for the current market status. """
    def __init__(self):
        Base.__init__(self)

        self._path = API_PATH['clock']
        self._payload = ''
        self._data = self._api_response(endpoint=self._endpoint,
                                        path=self._path,
                                        payload=self._payload)

    def _parse_response(self, attribute, **config):
        # returns the data from the API response in a dictionary for, {symbol0: data0, symbol1: data1, symbol2: data2}
        # overrides from Base super since response must be a dictionary

        if 'update' in list(config.keys()) and config['update'] is False:
            # update the data if the `update` parameter is true
            pass

        else:
            self.update_data()  # updates by default, user must specify to not update from the API

        return self._data['clock'][attribute]


    def date(self, **config):
        """ An ISO representation of the date in YYYY-MM-DD. """
        return self._parse_response('date', **config)

    def desc(self, **config):
        """ A short description of the market status. """
        return self._parse_response('description', **config)

    def next_change(self, **config):
        """ Returns the time of next state change. """
        return self._parse_response('next_change', **config)

    def next_state(self, **config):
        """ Returns the next state of the market (i.e. premarket, postmarket, etc.) """
        return self._parse_response('next_state', **config)

    def state(self, **config):
        """ Returns the current state of the market. """
        return self._parse_response('state', **config)

    def timestamp(self, **config):  # returns the timestamp of the last check
        """ Returns the timestamp of the status update. 
            
            The default style is Unix Epoch time, though using ``style='pretty'`` returns the time in ``YYYY-MM-DD H:M:S``
        """
        response = self._parse_response('timestamp', **config)

        if 'style' in list(config.keys()):
            # user has specified style of time response

            if config['style'] == 'epoch':
                return response  # API returns Unix epoch by default, so return raw response time value

            if config['style'] == 'pretty':  # useful for displaying the timestamp
                return time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(response))

        else:
            return response

        
"""  """        

