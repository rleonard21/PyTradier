from ..base import Base
from ..const import API_PATH

class Chain(Base):

    def __init__(self, symbol, expiration):
        """ Create an instance of the ``Chain`` class.
        
        :param symbol: The symbol for the options chain. By default, this is passed from the parent ``Company`` class. 
        :param expiration: The desired expiration for the options in the format ``YYY-MM-DD``. `Required.`
        
        .. note:: All options contracts expire on a Friday. If the requested expiration date is not a Friday, no data will be returned!
        
        Like many of the other functions PyTradier offers, ``Chain`` returns the data in the form of a dictionary with the 
        options symbol as the key and the requested data as the value.
        
        """
        Base.__init__(self)

        self._symbol = symbol
        self._expiration = expiration



        self._payload = {'symbol': self._symbol,
                         'expiration': self._expiration}

        self._path = API_PATH['chains']
        self._data = self._api_response(endpoint=self._endpoint,
                                        path=self._path,
                                        payload=self._payload)

        if self._data['options'] is not None:
            self._key = self._data['options']['option']
        else:
            self._key = []
        self._inner_key = 'symbol'


    def symbol(self, **config):
        """ Return the symbol of the contract. For example:
        
        .. code-block:: python
            
            chain = tradier.company('TSLA').chain()
            print chain.symbol()
        
        This will output a large options chain that looks similar to this:
        
        .. code-block:: python
        
            {TSLA170714C00292500: TSLA170714C00292500, TSLA170714C00295000: TSLA170714C00295000, ...}
            
        You can then get updates on particular contracts through the ``Option`` class using the output symbols from this method
        as the input for the ``Option`` class. 
        """
        return self._parse_response(attribute='symbol', **config)

    def strike(self, **config):
        """ Return the strike price for each contract. """
        return self._parse_response(attribute='strike', **config)

    def last(self, **config):
        """ Return the latest price for each contract. """
        return self._parse_response(attribute='last', **config)

    def bid(self, **config):
        """ Return the latest bid price for each contract. """
        return self._parse_response(attribute='bid', **config)

    def ask(self, **config):
        """ Return the latest ask price for each contract. """
        return self._parse_response(attribute='ask', **config)

    def change(self, **config):
        """ Return the latest change in price for each contract. """
        return self._parse_response(attribute='change', **config)

    def interest(self, **config):
        """ Return the open interest for each contract. """
        return self._parse_response(attribute='open_interest', **config)
