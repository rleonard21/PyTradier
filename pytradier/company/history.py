from ..base import Base
from ..const import API_PATH

class History(Base):
    """ A class for handling historical pricing of companies. """
    def __init__(self, symbol, interval=None, start=None, end=None):
        """ Create an instance of the History class. 
        
        :param symbol: The requested company symbol. By default, the parent ``Company`` class symbol is passed to this method. 
        :param interval: Interval of time for the requested data set. Defaults to ``'daily'``, but can also take ``weekly`` and ``monthly``.
        For example, if the interval is set to ``'monthly'``, then each piece of data represents one month. A smaller interval has more data. `Optional.` 
        :param start: The start date of the data set in the format ``YYYY-MM-DD``. `Optional.`
        :param end: The end date of the data set in the format ``YYYY-MM-DD``. `Optional.`
        
        .. note::
        
            Each method returns a dictionary with the date as the key and the requested data as the value. 
        
        """
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
        """ Return the date in ISO format ``YYYY-MM-DD``. """
        return self._parse_response(attribute='date', update=False)

    def open(self):
        """ Return the opening price for the interval. """
        return self._parse_response(attribute='open', update=False)

    def high(self):
        """ Return the highest price from the interval. """
        return self._parse_response(attribute='high', update=False)

    def low(self):
        """ Return the lowest point from the interval. """
        return self._parse_response(attribute='low', update=False)

    def volume(self):
        """ Return the total volume for the interval. """
        return self._parse_response(attribute='volume', update=False)



