from .calendar import Calendar
from .lookup import Lookup
from .search import Search
from .status import Status

class Market:

    def __init__(self, base):
        self.base = base

    def calendar(self, month=None, year=None):
        return Calendar(self.base, month, year)

    def lookup(self, **query):
        return Lookup(self.base, **query)

    def search(self, **query):
        return Search(self.base, **query)

    def status(self):
        return Status(self.base)
