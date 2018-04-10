from ..const import API_PATH

from ..base import Base

class Calendar(Base):
    """A class for obtaining dates and times for the market, handling both past and future dates.   
        
    .. note::
        The output of each method is a dictionary with a date as the key and the particular 
        value of the method as the value.
        
    """

    def __init__(self, month=None, year=None):
        """Create an instance of the Calendar class.
        
        :param month: Month of the calendar requested.
        :param year: Year of the calendar requested.
        
        Either one or both of ``month`` and ``year`` can be provided. The fetched calendar will only be as
        specific as you request. For example:
        
        .. code-block:: python
            
            calendar1 = tradier.market.calendar(month=12, year=2016)
            calendar2 = tradier.market.calendar(year=2017)
        
        ``calendar1`` will return a calendar of only December, 2016. ``calendar2``, on the other hand, will
        return a calendar for all of 2017. Future dates are also accepted.
        
        """
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
        """ Retrieve the month of the calendar. """
        return self._data['calendar']['month']

    def year(self, **config):
        """ Retrieve the year of the calendar. """
        return self._data['calendar']['year']

    def date(self, **config):
        """ Return the date in the format YYYY-MM-DD. """
        return self._parse_response(attribute='date', **config)

    def status(self, **config):
        """ Get the status of the market. """
        return self._parse_response(attribute='status', **config)

    def desc(self, **config):
        """ Returns a short description of the date. """
        return self._parse_response(attribute='description', **config)

    def open(self, **config):
        """ Returns a dictionary of the interval the market is open. Returns ``NoneType`` if the market is closed (i.e. Sunday, etc.). """
        return self._parse_response(attribute='open', **config)

    def premarket(self, **config):
        """ Returns a dictionary of the interval time for the premarket. Returns ``NoneType`` if there isn't a 
            premarket (i.e. Sunday, etc.). """
        return self._parse_response(attribute='premarket', **config)

    def postmarket(self, **config):
        """ Returns a dictionary of the interval time for postmarket. Returns ``NoneType`` if there isn't a 
                    postmarket (i.e. Sunday, etc.). """
        return self._parse_response(attribute='postmarket', **config)
