# from action import Action
# from calendar import Calendar
# from dividend import Dividend
# from info import Info
# from ratio import Ratio
# from report import Report
# from stats import Stats
from .chain import Chain
from .history import History
from .timesales import TimeSales
from .expirations import Expirations


class Company:
    def __init__(self, symbol):
        self._symbol = symbol

    def chain(self, expiration, greeks=bool):
        return Chain(self._symbol, expiration, greeks)

    def expirations(self):
        return Expirations(self._symbol)

    def history(self, interval=None, start=None, end=None):
        return History(self._symbol, interval, start, end)

    def timesales(self, interval=None, start=None, end=None, sfilter=None):
        return TimeSales(self._symbol, interval, start, end, sfilter)

    # Tradier has not yet implemented the following functions
    # into their API:

    # def action(self):
    #     return Action(symbol=self.__symbol)
    #
    # def calendar(self):
    #     return Calendar(symbol=self.__symbol)
    #
    # def dividend(self):
    #     return Dividend(symbol=self.__symbol)
    #
    # def info(self, period):
    #     return Info(symbol=self.__symbol, period=period)
    #
    # def ratio(self, period):
    #     return Ratio(symbol=self.__symbol, period=period)
    #
    # def report(self):
    #     return Report(symbol=self.__symbol)
    #
    # def stats(self, period):
    #     return Stats(symbol=self.__symbol, period=period)
