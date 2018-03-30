import os

from . import account
from . import company
from . import market
from . import order
from .config import get_auth
from .const import API_ENDPOINT
from .exceptions import ClientException
from .securities import stock, option


class Tradier:

	def __init__(self, **config):
		""" Create an instance of the ``Tradier`` class.
		There are two methods for authenticating with the Tradier API. The first method is to use a ``pytradier.ini``
		file with the correct credentials. The second way enables the user to authenticate directly in the script
		without the use of an external file.

		If the developer decides to use an external file to store credentials, the ``pytradier.ini`` file should be
		structured like this:

		.. code-block:: bash

			[AUTH]
			Token =
			AccountID =
			Endpoint =

		:param Token: The API access token provided by Tradier.
		:param AccountID: The ID associated with the Tradier brokerage account. If the developer does not have a
		brokerage account, this value should be set to ``None``.
		:param Endpoint: The chosen endpoint of the API. Use ``brokerage`` if the developer has a brokerage account and
		use ``sandbox`` if not.

		If the developer decides to leave credentials in the script, this method can be done using the following
		parameters:

		:param token: The API access token provided by Tradier.
		:param account_id: The ID associated with the Tradier brokerage account. If the developer does not have a
		brokerage account, this value should be set to ``None``.
		:param endpoint: The chosen endpoint of the API. Use ``brokerage`` if the developer has a brokerage account and
		use ``sandbox`` if not.

		In either case, an instance of the ``Tradier`` class must be created in order to access any part of the Tradier
		API, since the API is protected and the ``Tradier`` class contains your access token, account ID, and endpoint.

		.. code-block:: python

			tradier = Tradier(token='a1b2c3d4e5', account_id='0123456789', endpoint=None)

		From here, all parts of the PyTradier library can be access through your instance of the ``Tradier`` class.
		For example, to retrieve the current market status:

		.. code-block:: python

			print tradier.market.status()

		"""

		if 'auth' in config.keys():
			auth = get_auth(config['auth'])
			os.environ['API_TOKEN'] = auth[0]
			os.environ['API_ACCOUNT_ID'] = auth[1]

			try:
				os.environ['API_ENDPOINT'] = API_ENDPOINT[auth[2]]

			except KeyError:
				raise ClientException('Given endpoint not supported.')

		if 'token' in config.keys():
			os.environ['API_TOKEN'] = config['token']  # create environment variable for all files to use

		if 'account_id' in config.keys():  # environment variables must me type str
			os.environ['API_ACCOUNT_ID'] = config['account_id']

		if 'endpoint' in config.keys():  # user did not specify an endpoint

			try:
				os.environ['API_ENDPOINT'] = API_ENDPOINT[config['endpoint']]

			except KeyError:
				raise ClientException('Given endpoint not supported.')

		self.market = market.Market()

	def account(self):
		""" Provide an instance of ``account``. """
		return account.Account()

	def company(self, symbol):
		""" Provide an instance of ``company``. This is for accessing information about a company, including historical pricing
		for their stock. """
		return company.Company(symbol=symbol)

	def order(self):
		""" Provide an instance of ``order``. This is the class in which trading takes place. """
		return order.Order()

	def stock(self, *symbols):
		""" Provide an instance of ``stock``. This is the gateway to market data for stocks. """
		return stock.Stock(*symbols)

	def option(self, *symbols):
		""" Provide an instance of ``option``. This is the gateway to market data for options. """
		return option.Option(*symbols)
