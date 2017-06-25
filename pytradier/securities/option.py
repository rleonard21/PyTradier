from .quote import Quote
from ..base import Base
from ..const import API_ENDPOINT, API_PATH
import os



class Option(Quote):

    def __init__(self, *symbols):
        Base.__init__(self)
        Quote.__init__(self, *symbols)  # init the Quote and Base classes as supers


    def strike(self):
        data = self._api_quote('strike')

        return data

    def expiration(self):
        data = self._api_quote('expiration_date')

        return data

    def type(self):
        data = self._api_quote('option_type')

        return data

    def expiration_type(self):
        data = self._api_quote('expiration_type')

        return data

    def contract_size(self):
        data = self._api_quote('contract_size')

        return data

    def underlying(self):
        data = self._api_quote('underlying')

        return data

    def open_interest(self):
        data = self._api_quote('open_interest')

        return data

