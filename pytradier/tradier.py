
from const import API_ENDPOINT
from . import company

class Tradier:
    def __init__(self, token, account_id=None, endpoint=None):
        self.__token = token
        self.__account_id = account_id  # account_id is default to None for those without
        self.__endpoint = endpoint

        if self.__endpoint is None:  # user did not specify an endpoint
            self.__endpoint = API_ENDPOINT['sandbox']  # default endpoint is the sandbox

    def company(self, symbol):
        return company.Company(symbol=symbol)
