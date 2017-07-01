from .quote import Quote


class Option(Quote):

    def __init__(self, *symbols):
        Quote.__init__(self, *symbols)  # init the Quote and Base classes as supers

    def strike(self, **config):
        return self._api_quote(attribute='strike', **config)

    def expiration(self, **config):
        return self._api_quote(attribute='expiration_date', **config)

    def option_type(self, **config):
        return self._api_quote(attribute='option_type', **config)

    def expiration_type(self, **config):
        return self._api_quote(attribute='expiration_type', **config)

    def contract_size(self, **config):
        return self._api_quote(attribute='contract_size', **config)

    def underlying(self, **config):
        return self._api_quote(attribute='underlying', **config)

    def open_interest(self, **config):
        return self._api_quote(attribute='open_interest', **config)


