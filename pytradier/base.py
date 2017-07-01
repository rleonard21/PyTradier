import requests
import json
import os
from .exceptions import APIException

class Base(object):

    def __init__(self):
        self.__token = os.environ['API_TOKEN']
        self.__id = os.environ['API_ACCOUNT_ID']
        self._endpoint = os.environ['API_ENDPOINT']

        self._path = ''
        self._payload = ''
        self._data = ''

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

        try:
            j['fault']  # see if there is a fault message in the API response

        except KeyError:
            return j  # if no fault code, then return the API response

        # if there is a fault code, raise an API exception
        raise APIException(error_type=j['fault']['detail']['errorcode'],
                           error_message=j['fault']['faultstring'])

    def update_data(self):
        self._data = self._api_response(self._endpoint, self._path, self._payload)
        print self._data