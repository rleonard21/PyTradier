import requests
import json
import os
import time
from .exceptions import APIException

class Base(object):

    def __init__(self):
        """ Create an instance of the Base class. """
        self.__token = os.environ['API_TOKEN']
        self.__id = os.environ['API_ACCOUNT_ID']
        self._endpoint = os.environ['API_ENDPOINT']

        self._path = ''
        self._key = {}
        self._inner_key = ''
        self._payload = ''
        self._data = {}

        self.__last_updated = time.time()

    def _api_response(self, endpoint, path, payload):
        """ Retrieve the requested data from Tradier. This is the main function called by other classes to retrieve information.
        
        :param endpoint: The desired endpoint. By default, this is passed in from the intialization of the ``Tradier`` class.
            Accepts ``'developer_sandbox'``, ``'brokerage_sandbox'``, or ``'brokerage'``.
        :param path: The API path to information. By default, this is passed in from the inheriting class's endpoint. Endpoints
            are in the form ``/v1/markets/quotes``.
        :param payload: A dictionary of the information required to send to Tradier for API calls. For example, the Market Data endpoint
            requires ``{symbols: 'TSLA'}``.
        
        In general, this class shouldn't be accessed directly by the developer. Most classes inherit from Base and pass information
        in such as ``path``, ``endpoint``, and ``payload``.
        
        """
        
        headers = {"Accept": "application/json",
                   "Authorization": "Bearer " + self.__token}

        r = requests.request('GET', endpoint + path, headers=headers, params=payload)
        # print r.url
        # print r.headers
        # print 'remaining: ', r.headers['X-Ratelimit-Available']  # displays the remaining API calls for the interval
        # print r.content

        j = json.loads(r.content)
        # print j

        try:
            j['fault']  # see if there is a fault message in the API response

        except KeyError:
            return j  # if no fault code, then return the API response

        # if there is a fault code, raise an API exception
        raise APIException(error_type=j['fault']['detail']['errorcode'],
                           error_message=j['fault']['faultstring'])

    def update_data(self):
        self._data = self._api_response(self._endpoint, self._path, self._payload)
        self.__last_updated = time.time()  # updated the timestamp


    def _parse_response(self, attribute, **config):
        # returns the data from the API response in a dictionary for, {symbol0: data0, symbol1: data1, symbol2: data2}
        # overrides from Base super since response must be a dictionary

        if 'update' in list(config.keys()) and config['update'] is False:
            # update the data if the `update` parameter is true
            pass

        else:
            self.update_data()  # updates by default, user must specify to not update from the API

        response_load = {}

        if type(self._key) is not list:
            self._key = [self._key]
        for response in self._key:
            # more than one symbol supplied, loop through each one
            if attribute in list(response.keys()):
                response_load[response[self._inner_key]] = response[attribute]

            else:
                # this ensures that days when market is closed return None type if a market attribute is called.
                response_load[response[self._inner_key]] = None

        return response_load

    def timestamp(self):
        return self.__last_updated
    
    def _data(self, **config):
        """ Return the large, unorganized and unsorted data before PyTradier parses it. """
        return self._parse_response(**config)
        
