from ..base import Base
from ..const import API_PATH

class History(Base):
    def __init__(self, symbol, interval=None, start=None, end=None):
        Base.__init__(self)

        self._symbol = symbol
        self._interval = interval
        self._start = start
        self._end = end

        self._payload = {'symbol': self._symbol}

        if self._interval is not None:
            self._payload['interval'] = self._interval

        if self._start is not None:
            self._payload['start'] = self._start

        if self._end is not None:
            self._payload['end'] = self._end

        self._path = API_PATH['history']
        self._data = self._api_response(endpoint=self._endpoint,
                                        path=self._path,
                                        payload=self._payload)

        self._key = self._data['history']['day']
        self._inner_key = 'date'


    def date(self):
        return self._parse_response(attribute='date', update=False)

    def open(self):
        return self._parse_response(attribute='open', update=False)

    def high(self):
        return self._parse_response(attribute='high', update=False)

    def low(self):
        return self._parse_response(attribute='low', update=False)

    def volume(self):
        return self._parse_response(attribute='volume', update=False)



