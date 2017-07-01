from ..base import Base
from ..const import API_PATH

import datetime


class Status(Base):
    def __init__(self):
        Base.__init__(self)

        self._path = API_PATH['clock']
        self._key = 'clock'
        self._payload = ''
        self._data = self._api_response(endpoint=self._endpoint,
                                        path=self._path,
                                        payload=self._payload)






    def date(self, **config):
        return self._parse_response('date')

    def desc(self, **config):
        return self._parse_response('description')

    def next_change(self, **config):
        return self._parse_response('next_change')

    def next_state(self, **config):
        return self._parse_response('next_state')

    def state(self, **config):
        return self._parse_response('state')








    def timestamp(self, **config):  # None style defaults to returning epoch
        response = self._parse_response('timestamp')

        if 'style' in config.keys():
            # user has specified style of time response

            if config['style'] is 'epoch':
                return response  # API returns epoch by default, so return raw response time value



            pass




        else:
            print 'updating'
            self.update_data()  # updates by default, user must specify to not update from the API



#  timestamp(style=something)