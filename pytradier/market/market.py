from .calendar import Calendar
from .lookup import Lookup
from .search import Search
from .status import Status

class Market:

    def __init__(self):
        pass

    def calendar(self, month=None, year=None):
        return Calendar(month, year)

    def lookup(self, **query):
        return Lookup(**query)

    def search(self, **query):
        return Search(**query)

    def status(self):
        return Status()