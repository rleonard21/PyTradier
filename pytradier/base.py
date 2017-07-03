import requests
import json
import os
import time
from .exceptions import APIException

class Base(object):

    def __init__(self):
        self.__token = os.environ['API_TOKEN']
        self.__id = os.environ['API_ACCOUNT_ID']
        self._endpoint = os.environ['API_ENDPOINT']

        self._path = ''
        self._key = ''
        self._payload = ''
        self._data = {}

        self.__last_updated = time.time()

    def _api_response(self, endpoint, path, payload):

        # if not isinstance(payload, dict):  # payload must be in format payload={'hello': 'world'}
        #     raise TypeError

        headers = {"Accept": "application/json",
                   "Authorization": "Bearer " + self.__token}

        r = requests.request('GET', endpoint + path, headers=headers, params=payload)
        # print r.url
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

        if 'update' in config.keys() and config['update'] is False:
            # update the data if the `update` parameter is true
            pass

        else:
            self.update_data()  # updates by default, user must specify to not update from the API

        return self._data[self._key][attribute]

    def timestamp(self):
        return self.__last_updated
