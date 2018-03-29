from ..base import Base
from ..const import API_PATH
import time


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

			Each method (except ``bundle``) returns a dictionary with the date as the key and the requested data as the
			value. Dictionaries are `unordered`.

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

	def date(self, **config):
		""" Return the date in ISO format ``YYYY-MM-DD``. """
		return self._parse_response(attribute='date', **config)

	def open(self, **config):
		""" Return the opening price for the interval. For example, is interval is ``daily``, the open
			price will be the price at market open, and the closing price is the price at market close.
		"""
		return self._parse_response(attribute='open', **config)

	def close(self, **config):
		""" Return the closing price for the interval. """
		return self._parse_response(attribute='close', **config)

	def high(self, **config):
		""" Return the highest price from the interval. """
		return self._parse_response(attribute='high', **config)

	def low(self, **config):
		""" Return the lowest point from the interval. """
		return self._parse_response(attribute='low', **config)

	def volume(self, **config):
		""" Return the total volume for the interval. """
		return self._parse_response(attribute='volume', **config)

	def bundle(self, reverse_sort=False):
		""" Returns a multi-dimension list of all data, sorted by ascending by default.
		Each element is in the form, ``[epoch, open, close, high, low, volume]``.

		:param reverse_sort: Determines the order of sorting the data. Default is False, which sorts by ascending dates.

		This method can be useful for machine learning or other data handling methods since this returns a list of
		numbers, rather than a dictionary with keys.

		Example:

		.. code-block:: python

			company = tradier.company(symbol='AAPL')
			history = company.history(interval='monthly', start='2011-1-1', end='2012-1-1')
			print(history.bundle(reverse_sort=True))

		The above code will output a multi-dimension list with descending dates:

		.. code-block:: python

			[[1325394000, 58.485714, 64.715714, 64.921429, 58.428571, 1617345800],
			[1322715600, 54.648571, 57.857143, 58.441429, 53.954286, 1577342800], ...]

		"""

		bundle = []
		raw_data = self._data['history']['day']  # raw Tradier API response

		for data in raw_data:
			epoch = int(time.mktime(time.strptime(data['date'], '%Y-%m-%d')))  # convert to epoch from date string

			bundle.append([epoch, data['open'], data['close'], data['high'], data['low'], data['volume']])

		bundle.sort(key=lambda r: r[0], reverse=reverse_sort)  # sort by the given method

		return bundle
