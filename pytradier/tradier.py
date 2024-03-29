
from .const import API_ENDPOINT

from .base import Base
from . import company
from . import account
from . import order
from . import market

from .securities import stock, option

from .exceptions import ClientException

import os
# from . import user



class Tradier:

    def __init__(self, token, account_id=None, endpoint=None):
        """ Create an instance of the ``Tradier`` class. 
        
        :param token: The API access token provided by Tradier. `Required.`
        :param account_id: The ID associated with your Tradier brokerage account. If not provided, you will only
        be able to access market data. 
        :param endpoint: The chosen endpoint. If not provided, it defaults to using the full API. For developer only
        accounts, you must specify ``endpoint='developer_sandbox'``.
        
        An instance of the ``Tradier`` class must be created in order to access any part of the Tradier API,
        since the API is protected and the ``Tradier`` class contains your access token, account ID, and endpoint. 
        
        .. code-block:: python
        
            tradier = Tradier(token='a1b2c3d4e5', account_id='0123456789', endpoint=None)
        
        From here, all parts of the PyTradier library can be access through your instance of the ``Tradier`` class. 
        For example, to retrieve the current market status:
        
        .. code-block:: python
        
            print tradier.market.status()  # output: open
        
        
        
        
        
        """

        endpoint = API_ENDPOINT[endpoint] if endpoint is not None else API_ENDPOINT['developer_sandbox']
        self.__base = Base(token, account_id, endpoint)
        self.market = market.Market(self.__base)
        self.Account = account.Account(self.__base)
        self.Order = order.Order(self.__base)

    def account(self):
        """ Provide an instance of ``account``. """
        return self.Account

    def company(self, symbol):
        """ Provide an instance of ``company``. This is for accessing information about a company, including historical pricing
        for their stock. """
        return company.Company(self.__base, symbol=symbol)

    def order(self):
        """ Provide an instance of ``order``. This is the class in which trading takes place. """
        return self.Order

    def stock(self, *symbols):
        """ Provide an instance of ``stock``. This is the gateway to market data for stocks. """
        return stock.Stock(self.__base, *symbols)

    def option(self, *symbols):
        """ Provide an instance of ``option``. This is the gateway to market data for options. """
        return option.Option(self.__base, *symbols)
