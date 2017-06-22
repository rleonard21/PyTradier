from balance import Balance
from costbasis import CostBasis
from history import History
from orders import Orders
from orderstatus import OrderStatus
from positions import Positions

class Account:
    def __init__(self):
        pass


    def balance(self):
        return Balance()

    def costbasis(self):
        return CostBasis()

    def history(self):
        return History()

    def orders(self):
        return Orders()

    def orderstatus(self):
        return OrderStatus()

    def positions(self):
        return Positions()