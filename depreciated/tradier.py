from . import market

class Tradier:

    def __init__(self, endpoint, token, account_id=None, ):
        self.endpoint = endpoint
        self.token = token
        self.account_id = account_id


    # ETFs ==========
    def etf(self, symbol):
        return market.etf.ETF(symbol)

    def option(self, symbol=None, expiration=None):
        return market.Option(symbol, expiration)


    # def calendar(self, month=None, year=None):
    #     return market_data.Calendar(month, year)
    #
    # def clock(self):
    #     return market_data.Clock()
    #
    # def history(self, symbol, interval=None, start=None, end=None):
    #     return market_data.History(symbol, interval, start, end)
    #
    # def lookup(self, symbol=None, exchange=None, types=None):  # at least one is required
    #     return market_data.Lookup()
    #
    # def quote(self, symbol):
    #     return market_data.Quote(symbol)
    #
    # def search(self, keyword, indexes=False):
    #     return market_data.Search()
    #
    # def stream(self):
    #     return market_data.Stream()
    #
    # def timesales(self, symbol, interval, start, end, session_filter):
    #     return market_data.TimeSale(symbol, interval, start, end, session_filter)


    # Options ========

    # def chain(self, symbol, expiration):
    #     return market_data.Chain(symbol, expiration)
    #
    # def strike(self, symbol, expiration):
    #     return market_data.Strike(symbol, expiration)
    #
    # def expiration(self, symbol):
    #     return market_data.Expiration(symbol)

