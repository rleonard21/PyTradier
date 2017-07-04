from ..base import Base
from ..const import API_PATH

class TimeSales(Base):
    def __init__(self, symbol, interval=None, start=None, end=None, sfilter=None):
        Base.__init__(self)

        self._symbol = symbol
        self._interval = interval
        self._start = start
        self._end = end
        self._filter = sfilter

        self._payload = {'symbol': self._symbol}

        if self._interval is not None:
            self._payload['interval'] = self._interval

        if self._start is not None:
            self._payload['start'] = self._start

        if self._end is not None:
            self._payload['end'] = self._end

        if self._filter is not None:
            self._payload['session_filter'] = self._filter

        self._path = API_PATH['timesales']
        self._data = self._api_response(endpoint=self._endpoint,
                                        path=self._path,
                                        payload=self._payload)

        self._key = self._data['series']['data']
        self._inner_key = 'time'


    def time(self, **config):
        return self._parse_response(attribute='time', **config)

    def open(self, **config):
        return self._parse_response(attribute='open', **config)

    def close(self, **config):
        return self._parse_response(attribute='close', **config)

    def high(self, **config):
        return self._parse_response(attribute='high', **config)

    def low(self, **config):
        return self._parse_response(attribute='low', **config)

    def volume(self, **config):
        return self._parse_response(attribute='volume', **config)



