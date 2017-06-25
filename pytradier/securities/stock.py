from .quote import Quote

class Stock(Quote):

    def __init__(self, *symbols):
        Quote.__init__(self, *symbols)  # init the Quote classes as supers
