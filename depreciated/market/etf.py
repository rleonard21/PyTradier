from calendar import Calendar
from clock import Clock
from history import History
from lookup import Lookup
from quote import Quote
from search import Search
from timesale import TimeSale


class ETF:
    def __init__(self, symbol):
        self.__symbol = symbol

    def history(self, interval=None, start=None, end=None):
        return History(self.__symbol, interval, start, end)

    def lookup(self, symbol=None, exchange=None, types=None):  # at least one is required
        return Lookup()

    def quote(self):
        return Quote(self.__symbol)

    def timesales(self, interval, start, end, session_filter):
        return TimeSale(self.__symbol, interval, start, end, session_filter)



