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

        self._key = self._data['calendar']['days']['day']
        self._inner_key = 'date'

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