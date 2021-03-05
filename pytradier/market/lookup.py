from ..base import Base
from ..const import API_PATH

class Lookup(Base):
    """ A class for looking up symbols or partial symbols. The results are listed by highest volume. 
    The results are a dictionary with the symbol as the key and the information from each method as the value. 
    """
    def __init__(self, **query):
        """ Create an instance for the symbol lookup. 
        
        :param symbol: The requested search symbol. It can be a full or partial symbol. 
        :param type: The type of symbol requested: ``stock``, ``etf``
        :param exchange: The exchange of the symbol. As of current, only Tradier exchange symbols are accepted. 
        
        Any combination of these three parameters can be used to create a search. The results of the search are
        stored in the instance of the class, which allows for the local storage of results rather than having to call to the API
        for each piece of information. 
        
        This gives you a wide range of abilities. For example, to retrieve `every` stock on the NYSE, use the argument ``exchange='A'``
        ('A' is the Tradier exchange code for NYSE), and ignore the other parameters:
        
        .. code-block:: python
        
            nyse = tradier.market.lookup(exchange='A')
            print nyse.symbol
        
        And the result is a long dictionary, sorted by largest volume:
        
        .. code-block:: python
        
            {BAC: BAC, TWTR: TWTR, RAD: RAD, ... }
        
        
        
        """
        Base.__init__(self)

        self._payload = {}

        if 'symbol' in list(query.keys()):
            self._payload['q'] = query['symbol']

        if 'type' in list(query.keys()):
            self._payload['type'] = query['type']

        if 'exchange' in list(query.keys()):
            self._payload['exchanges'] = query['exchange']

        self._path = API_PATH['lookup']
        self._data = self._api_response(endpoint=self._endpoint,
                                        path=self._path,
                                        payload=self._payload)

        if self._data['securities'] is not None:
            self._key = self._data['securities']['security']
        else:
            self._key = []
        self._inner_key = 'symbol'


    def symbol(self, **config):
        """ Return the symbol from the search. 
        | For example:
        
        .. code-block:: python
        
            tradier.market.lookup(symbol='AAPL').symbol()
        """
        return self._parse_response(attribute='symbol', **config)

    def exchange(self, **config):
        """ Return the exchange of the symbol. 
        | For example:
        
        .. code-block:: python
        
            tradier.market.lookup(symbol='AAPL').exchange()
            
        .. note::
        
            Exchanges are returned as symbols according to Tradier's naming system of exchanges. 
        """
        return self._parse_response(attribute='exchange', **config)

    def type(self, **config):
        """ Return the type of symbol (``stock``, ``etf``, ``index``). 
        | For example:
        
        .. code-block:: python
        
            tradier.market.lookup(symbol='AAPL').type()
        
        """
        return self._parse_response(attribute='type', **config)

    def desc(self, **config):
        """ Return a short description of the symbol. 
        | For example:
        
        .. code-block:: python
        
            tradier.market.lookup(symbol='AAPL').desc()
        """
        return self._parse_response(attribute='description', **config)
  
