from .quote import Quote


class Option(Quote):

    def __init__(self, *symbols):
        Quote.__init__(self, *symbols)  # init the Quote and Base classes as supers

    def strike(self, **config):
        return self._parse_response(attribute='strike', **config)

    def expiration(self, **config):
        return self._parse_response(attribute='expiration_date', **config)

    def option_type(self, **config):
        return self._parse_response(attribute='option_type', **config)

    def expiration_type(self, **config):
        return self._parse_response(attribute='expiration_type', **config)

    def contract_size(self, **config):
        return self._parse_response(attribute='contract_size', **config)

    def underlying(self, **config):
        return self._parse_response(attribute='underlying', **config)

    def open_interest(self, **config):
        return self._parse_response(attribute='open_interest', **config)


