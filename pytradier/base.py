import requests
import json
import credentials


def API_response(endpoint, path, payload):

    if not isinstance(payload, dict):  # payload must be in format payload={'hello': 'world'}
        raise TypeError

    headers = {"Accept": "application/json",
               "Authorization": "Bearer " + credentials.ACCESS_TOKEN
               }

    payload = {'symbols': 'AAPL'}

    r = requests.request('GET', endpoint + path, headers=headers, params=payload)
    print r.url

    j = json.loads(r.content)

    return j


