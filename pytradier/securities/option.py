from .quote import Quote


class Option(Quote):

    def __init__(self, *symbols):
        Quote.__init__(self, *symbols)  # init the Quote and Base classes as supers


    def strike(self):
        return self._api_quote('strike')

    def expiration(self):
        return self._api_quote('expiration_date')

    def option_type(self):
        return self._api_quote('option_type')

    def expiration_type(self):
        return self._api_quote('expiration_type')

    def contract_size(self):
        return self._api_quote('contract_size')

    def underlying(self):
        return self._api_quote('underlying')

    def open_interest(self):
        return self._api_quote('open_interest')


