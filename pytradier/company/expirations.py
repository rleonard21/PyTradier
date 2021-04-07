from ..base import Base
from ..const import API_PATH

class Expirations(Base):

    def __init__(self, symbol):
        """ Create an instance of the ``Expirations`` class.
        
        :param symbol: The symbol to return options expirations for. By default, this is passed from the parent ``Company`` class.              
        
        """
        Base.__init__(self)

        self._symbol = symbol

        self._payload = {'symbol': self._symbol}

        self._path = API_PATH['expirations']
        self._data = self._api_response(endpoint=self._endpoint,
                                        path=self._path,
                                        payload=self._payload)

        self._key = self._data['expirations']
        self._inner_key = 'date'

    def _parse_response(self, attribute, **config):
        if 'update' in list(config.keys()) and config['update'] is False:
            pass
        else:
            # update the data if the `update` parameter is true
            self.update_data()  # updates by default, user must specify to not update from the API
        if self._data['expirations'] is not None:
            return self._data['expirations']['date']
        return []

    def date(self, **config):
        """ Return the list of expirations dates for the symbol. """
        return self._parse_response(attribute='date', **config)
