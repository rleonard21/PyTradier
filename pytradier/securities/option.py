from .quote import Quote


class Option(Quote):
    """ A class for fetching and storing market data for options. """
    
    def __init__(self, *symbols):
        """ Create an instance of the Option class. 
        
        :param symbols: The symbol(s) of the options contract(s) to track. 
        
        One or more standard symbols can be used to create in instance:
        
        .. code-block:: python
        
            options = tradier.Option('TSLA170707C00295000', 'F170714C00010500')
            print options.underlying()
        
        The result is a dictionary:
        
        .. code-block:: python
        
            {TSLA: TSLA, F:F}
        
        
        """
        Quote.__init__(self, *symbols)  # init the Quote and Base classes as supers

    def strike(self, **config):
        """ Return the strike price of the option. """
        return self._parse_response(attribute='strike', **config)

    def expiration(self, **config):
        """ Return the expiration. """
        return self._parse_response(attribute='expiration_date', **config)

    def option_type(self, **config):
        """ Return the option type (``put`` or ``call``). """
        return self._parse_response(attribute='option_type', **config)

    def expiration_type(self, **config):
        """ Return the type of expiration (``standard``, ``weeklys``). """
        return self._parse_response(attribute='expiration_type', **config)

    def contract_size(self, **config):
        """ Return the size of the contract. """
        return self._parse_response(attribute='contract_size', **config)

    def underlying(self, **config):
        """ Return the underlying symbol for the contract. """
        return self._parse_response(attribute='underlying', **config)

    def open_interest(self, **config):
        """ Return the open interest for the contract. """
        return self._parse_response(attribute='open_interest', **config)


