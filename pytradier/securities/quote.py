from ..base import Base
from ..const import API_PATH
from ..const import EXCHANGE_CODES


class Quote(Base):
	# Super class for quotes

	def __init__(self, *symbols):
		Base.__init__(self)

		self._symbols = []

		for symbol in symbols:
			self._symbols.append(symbol)

		self._symbol_load = ','.join(self._symbols)

		self._path = API_PATH['quotes']
		self._payload = {'symbols': self._symbol_load}
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

		response_load = {}

		if len(self._symbols) == 1:
			# if there is only one symbol supplied, add it to the dictionary
			response_load[self._data['quotes']['quote']['symbol']] = self._data['quotes']['quote'][attribute]

		else:

			for quote in self._data['quotes']['quote']:
				# more than one symbol supplied, loop through each one

				response_load[quote['symbol']] = quote[attribute]

		return response_load

	def add_symbols(self, *symbols, **config):
		""" Add one or more symbols to the array of tracked symbols.

		:param symbols: A string containing the company's symbol.

		Multiple symbols can be added at once:

		.. code-block:: python

			stocks = tradier.Stock('AAPL', 'MSFT')  # create instance of the Stock class
			print stocks.symbol()  # output: {AAPL: AAPL, MSFT: MSFT}

			stocks.add_symbols('GOOG', 'TSLA')
			print stocks.symbol()  # output: {AAPL: AAPL, MSFT: MSFT, GOOG: GOOG, TSLA: TSLA}

		"""
		# adds a given symbol to the array of tracked symbols. the `update` parameter chooses whether or not to
		# call the API for new data

		for symbol in symbols:  # iterate through each new symbol
			self._symbols.append(symbol)

		self._symbol_load = ','.join(self._symbols)  # change form from array to CSV: [AAPL, MSFT] -> AAPL,MSFT
		self._payload = {'symbols': self._symbol_load}  # prepare the payload

		if 'update' in list(config.keys()) and config['update'] is False:
			# update the data if the `update` parameter is true
			pass

		else:
			self.update_data()  # updates by default, user must specify to not update from the API

	def symbol(self, **config):
		""" Return the symbol of each key in the dictionary. """
		return self._parse_response(attribute='symbol', **config)

	def desc(self, **config):
		""" Return a short description for each symbol. """
		return self._parse_response(attribute='description', **config)

	def exchange(self, **config):
		""" Return the exchange on which the symbol is traded.

		.. note::

			This returns a symbol according to Tradier's exchange codes

		"""
		# TODO: config option to return symbol name (NYSE, NASDAQ, etc.) or Tradier symbol (A, B, C, etc.)
		return self._parse_response(attribute='exch', **config)

	def type(self, **config):
		return self._parse_response(attribute='type', **config)

	def change(self, **config):
		""" Return the dollar change. """
		return self._parse_response(attribute='change', **config)

	def change_percentage(self, **config):
		""" Return the percentage change """
		return self._parse_response(attribute='change_percentage', **config)

	def volume(self, **config):
		""" Return the volume for the day. """
		return self._parse_response(attribute='volume', **config)

	def average_volume(self, **config):
		""" Return the average volume. """
		return self._parse_response(attribute='average_volume', **config)

	def last_volume(self, **config):
		""" Return the latest volume. """
		return self._parse_response(attribute='last_volume', **config)

	def trade_date(self, **config):
		""" Return the date and time of last trade in Unix Epoch time. """
		return self._parse_response(attribute='trade_date', **config)

	def open(self, **config):
		""" Return the opening price. """
		return self._parse_response(attribute='open', **config)

	def high(self, **config):
		""" Return the trading day high. """
		return self._parse_response(attribute='high', **config)

	def low(self, **config):
		""" Return the trading day low. """
		return self._parse_response(attribute='low', **config)

	def close(self, **config):
		""" Return the closing price. """
		return self._parse_response(attribute='close', **config)

	def prevclose(self, **config):
		""" Return the previous closing price. """
		return self._parse_response(attribute='prevclose', **config)

	def week_52_high(self, **config):
		""" Return the 52 week high. """
		return self._parse_response(attribute='week_52_high', **config)

	def week_52_low(self, **config):
		""" Return the 52 week low. """
		return self._parse_response(attribute='week_52_low', **config)

	def bid(self, **config):
		""" Return the latest bid price. """
		return self._parse_response(attribute='bid', **config)

	def bidsize(self, **config):
		""" Return the size of the current bid. """
		return self._parse_response(attribute='bidsize', **config)

	def bidexch(self, full_name=False, **config):
		""" Return the exchange of the current bid. This will return a dictionary of each symbol and the respective
		exchange code. The ``full_name`` parameter can be specified to return the name of the exchange rather
		than the exchange code. For example:

		.. code-block:: python

			stock = tradier.stock('AAPL', 'TSLA')
			print(stock.bidexch())
			print(stock.bidexch(full_name=True))

		This will return the following dictionaries:

		.. code-block:: python

			{'AAPL': 'Q', 'TSLA': 'Z'}
			{'AAPL': 'NASDAQ OMX', 'TSLA': 'BATS'}

		"""
		response = self._parse_response(attribute='bidexch', **config)

		if full_name is True:
			response_payload = {}
			for symbol in self._symbols:
				code = response[symbol]
				response_payload[symbol] = EXCHANGE_CODES[code]

			return response_payload

		else:
			return response

	def bid_date(self, **config):
		""" Return the date and time of the latest bid in Unix Epoch time. """
		return self._parse_response(attribute='bid_date', **config)

	def ask(self, **config):
		""" Return the latest ask price. """
		return self._parse_response(attribute='ask', **config)

	def asksize(self, **config):
		""" Return the size of the current ask. """
		return self._parse_response(attribute='asksize', **config)

	def askexch(self, full_name=False, **config):
		""" Return the exchange of the current ask. This will return a dictionary of each symbol and the respective
		exchange code. The ``full_name`` parameter can be specified to return the name of the exchange rather
		than the exchange code. For example:

		.. code-block:: python

			stock = tradier.stock('AAPL', 'TSLA')
			print(stock.bidexch())
			print(stock.bidexch(full_name=True))

		This will return the following dictionaries:

		.. code-block:: python

			{'AAPL': 'Q', 'TSLA': 'Z'}
			{'AAPL': 'NASDAQ OMX', 'TSLA': 'BATS'}

		"""
		response = self._parse_response(attribute='askexch', **config)

		if full_name is True:
			response_payload = {}
			for symbol in self._symbols:
				code = response[symbol]
				response_payload[symbol] = EXCHANGE_CODES[code]

			return response_payload

		else:
			return response

	def ask_date(self, **config):
		""" Return the date and time of the latest ask in Unix Epoch time. """
		return self._parse_response(attribute='ask_date', **config)
