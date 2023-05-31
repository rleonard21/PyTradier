from .quote import Quote

class Stock(Quote):
    """ A class for fetching and storing market data for stocks. """
    def __init__(self, base, *symbols):
        self.__dict__.update(base.__dict__)
