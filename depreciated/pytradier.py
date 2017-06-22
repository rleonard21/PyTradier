from . import models

class PyTradier:

    def __init__(self, token, account_id, endpoint):
        self.token = token
        self.account_id = account_id
        self.endpoint = endpoint

    def calendar(self, month=None, year=None):
        return models.Calendar(month, year)

    def clock(self):
        return models.Clock()

    def history(self, symbol, interval=None, start=None, end=None):
        return models.History(symbol, interval, start, end)

    def lookup(self, symbol=None, exchange=None, types=None):  # at least one is required
        return models.Lookup()

    def quote(self, symbol):
        return models.Quote(symbol)

    def search(self, keyword, indexes=False):
        return models.Search()

    def stream(self):
        return models.Stream()

    def timesales(self, symbol, interval, start, end, session_filter):
        return models.TimeSale(symbol, interval, start, end, session_filter)




    def chain(self, symbol, expiration):
        return models.option.Chain(symbol, expiration)

    def strike(self, symbol, expiration):
        return models.option.Strike(symbol, expiration)

    def expiration(self, symbol):
        return models.option.Expiration(symbol)

