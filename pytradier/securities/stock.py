from .quote import Quote

class Stock(Quote):
    """ A class for fetching and storing market data for stocks. """
    def __init__(self, *symbols):
        Quote.__init__(self, *symbols)  # init the Quote classes as supers
