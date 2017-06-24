import requests
import json
import os


class Base(object):

    def __init__(self):
        self.__token = os.environ['API_TOKEN']
        self.__id = os.environ['API_ACCOUNT_ID']



    def _api_response(self, endpoint, path, payload):

        if not isinstance(payload, dict):  # payload must be in format payload={'hello': 'world'}
            raise TypeError

        headers = {"Accept": "application/json",
                   "Authorization": "Bearer " + self.__token}

        r = requests.request('GET', endpoint + path, headers=headers, params=payload)
        # print r.url
        # print 'remaining: ', r.headers['X-Ratelimit-Available']  # displays the remaining API calls for the interval

        j = json.loads(r.content)

        return j


