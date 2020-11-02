from ..base import Base
from ..const import API_PATH

class TimeSales(Base):
    def __init__(self, symbol, interval=None, start=None, end=None, sfilter=None):
        """ Create an instance of the TimeSales class.
        
        :param symbol: The company symbol. By default, this is passed in from the parent ``Company`` class. 
        :param interval: The time interval between each sale. Options include ``'tick'``, ``'1min'``, ``'5min'``, and ``'15min'``. `Optional.`
        :param start: Start datetime for timesales range represented as ``YYYY-MM-DD HH:MM``. `Optional`.
        :param end: End date for timesales range represented as ``YYYY-MM-DD HH:MM``. `Optional`.
        :param sfilter: The session conditions to requetst data for. Defaults to ``'all'`` for all available data points.
                        Use ``'open'`` for data points within open market hours only. `Optional.`
        
        
        
        
        """
        
        
        
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
        """ Return the time of the data. """
        return self._parse_response(attribute='time', **config)

    def open(self, **config):
        """ Return the price of the start of the data interval. For example, if ``interval`` was set to ``'15min'``, 
            the opening price for that interval would the from the start of the 15 minute interval, and the closing price
            would be from the end of the interval. """
        return self._parse_response(attribute='open', **config)

    def close(self, **config):
        """ Return the price of the end of the data interval. """
        return self._parse_response(attribute='close', **config)

    def high(self, **config):
        """ Return the highest price from the interval. """
        return self._parse_response(attribute='high', **config)

    def low(self, **config):
        """ Return the lowest price of the interval. """
        return self._parse_response(attribute='low', **config)
    
    def price(self, **config):
        """ Return the last price of the interval. """
        return self._parse_response(attribute='price', **config)

    def volume(self, **config):
        """ Return the total volume of the interval. """
        return self._parse_response(attribute='volume', **config)
    
    def vwap(self, **config):
        """ Return the volume weighted average price of the interval. """
        return self._parse_response(attribute='vwap', **config)
    



