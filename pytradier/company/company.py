# from action import Action
# from calendar import Calendar
# from dividend import Dividend
# from info import Info
# from ratio import Ratio
# from report import Report
# from stats import Stats

from ..securities.option import Option
from ..securities.stock import Stock


class Company:
    def __init__(self, symbol):
        self.__symbol = symbol


    # def stock(self):
    #     # Returns an instance of the stock class and uses the same ticker from the company
    #
    #     return securities.Stock(self.__symbol)
    #
    # def option(self, *symbols):
    #     # returns instance of option class and requires an Option symbol and the expiration for the option
    #     # both of these can be found using the chain() function: Company.chain()
    #     # for example:  Company.option('SPY140627C00195500')
    #
    #     return securities.Option(*symbols)
    #
    #


    def chain(self):
        pass

    def strikes(self):
        pass

    def expirations(self):
        pass



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
