from .balance import Balance
from .costbasis import CostBasis
from .history import History
from .orders import Orders
from .orderstatus import OrderStatus
from .positions import Positions
from ..const import API_ENDPOINT
from ..exceptions import ClientException
import os


class Account:
    def __init__(self):
        if os.environ['API_ENDPOINT'] != API_ENDPOINT['brokerage']:
            # This part of the API only works with the full brokerage API, so require the 'brokerage' API endpoint.
            raise ClientException('Bad Endpoint: account paths require the full API (no sandbox!)')

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
