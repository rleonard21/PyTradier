from pytradier.base import Base
from pytradier.const import API_ENDPOINT, API_PATH
import os

class Option(Base):

    def __init__(self, symbol):
        super(Option, self).__init__()  # initialize from the super class, Base

        self.__symbol = symbol

        self.__payload = {'symbols': self.__symbol}

    def strike(self):
        response = self._api_response(endpoint=API_ENDPOINT['sandbox'],
                                      path=API_PATH['quotes'],
                                      payload=self.__payload)

        return response['quotes']['quote']['strike']

    def expiration(self):
        response = self._api_response(endpoint=API_ENDPOINT['sandbox'],
                                      path=API_PATH['quotes'],
                                      payload=self.__payload)

        return response['quotes']['quote']['expiration_date']

    def type(self):
        response = self._api_response(endpoint=API_ENDPOINT['sandbox'],
                                      path=API_PATH['quotes'],
                                      payload=self.__payload)

        return response['quotes']['quote']['option_type']

    def expiration_type(self):
        response = self._api_response(endpoint=API_ENDPOINT['sandbox'],
                                      path=API_PATH['quotes'],
                                      payload=self.__payload)

        return response['quotes']['quote']['expiration_type']

    def contract_size(self):
        response = self._api_response(endpoint=API_ENDPOINT['sandbox'],
                                      path=API_PATH['quotes'],
                                      payload=self.__payload)

        return response['quotes']['quote']['contract_size']

    def underlying(self):
        response = self._api_response(endpoint=API_ENDPOINT['sandbox'],
                                      path=API_PATH['quotes'],
                                      payload=self.__payload)

        return response['quotes']['quote']['underlying']

    def open_interest(self):
        response = self._api_response(endpoint=API_ENDPOINT['sandbox'],
                                      path=API_PATH['quotes'],
                                      payload=self.__payload)

        return response['quotes']['quote']['open_interest']
