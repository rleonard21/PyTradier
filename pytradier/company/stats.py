from .. import base
from ..const import API_ENDPOINT, API_PATH

class Stats:

    def __init__(self, symbol, period):
        self.__symbol = symbol
        self.__period = period

        self.__path = API_PATH['statistics']
        self.__payload = {'symbols': 'aapl'}


    # TODO: Error raising- some of these aren't returned every time

    def share_class_id(self):
        pass

    def as_of_date(self):
        pass

    def period(self):
        pass

    def closest_to_moving_average(self):
        pass

    def moving_average(self):
        j = base.API_response(endpoint=API_ENDPOINT['brokerage'], path=self.__path, payload=self.__payload)
        return j


        pass



    def non_div_alpha(self):
        pass

    def non_div_beta(self):
        pass

    def average_volume(self):
        pass

    def high(self):
        pass

    def low(self):
        pass

    def percent_below_high(self):
        pass

    def total_volume(self):
        pass



