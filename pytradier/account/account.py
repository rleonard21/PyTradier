from ..const import API_ENDPOINT
from ..exceptions import ClientException

from ..base import Base
from ..const import API_PATH

from .balance import Balance
from .order import Order
from .position import Position
from .costbasis import ClosedPosition
from .history import History

import os


class Account(Base):
	def __init__(self):
		Base.__init__(self)

		if os.environ['API_ENDPOINT'] not in [API_ENDPOINT['brokerage'], API_ENDPOINT['brokerage_sandbox']]:
			# This part of the API only works with the full brokerage API, so require a 'brokerage' API endpoint.
			raise ClientException('Bad Endpoint: account paths require the full API or brokerage sandbox (no developer sandbox!)')

	def balance(self):
		return Balance()

	def costbasis(self):
		self._path = API_PATH['account_gainloss'].replace('{account_id}', os.environ['API_ACCOUNT_ID'])
		self._data = self._api_response(endpoint=self._endpoint, path=self._path, payload=self._payload)
		
		try:
			self._key = self._data['gainloss']['closed_position']
		
		except TypeError:
			return None
		
		closed_positions = []
		
		for cp in self._key:
			new_closed_position = ClosedPosition(open_date=cp['open_date'], close_date=cp['close_date'],
			                                     term=cp['term'], cost=cp['cost'], gl=cp['gain_loss'],
			                                     gl_percent=cp['gain_loss_percent'], proceeds=cp['proceeds'],
			                                     quantity=cp['quantity'], symbol=cp['symbol'])
			
			closed_positions.append(new_closed_position)
		
		return closed_positions
	
	def history(self, limit=25):
		return History(limit)
	
	def orders(self):
		self._path = API_PATH['account_orders'].replace('{account_id}', os.environ['API_ACCOUNT_ID'])
		self._data = self._api_response(endpoint=self._endpoint, path=self._path, payload=self._payload)
		
		try:
			self._key = self._data['orders']['order']
		
		except TypeError:
			return None

		orders = []

		for o in self._key:
			new_order = Order(order_id=o['id'], order_type=o['type'], symbol=o['symbol'], side=o['side'],
							quantity=o['quantity'], status=o['status'], duration=o['duration'], price=o['price'],
							avg_fill_price=o['avg_fill_price'], exec_quantity=o['exec_quantity'],
							last_fill_price=o['last_fill_price'], last_fill_quantity=o['last_fill_quantity'],
							remaining_quantity=o['remaining_quantity'], create_date=o['create_date'],
							transaction_date=o['transaction_date'], class_type=o['type'])
			
			orders.append(new_order)

		return orders

	def positions(self):
		"""
		:return: Returns a list of Position objects.
		"""

		self._path = API_PATH['account_positions'].replace('{account_id}', os.environ['API_ACCOUNT_ID'])
		self._data = self._api_response(endpoint=self._endpoint, path=self._path, payload=self._payload)
		
		try:
			self._key = self._data['positions']['position']
			
		except TypeError:
			return None

		positions = []
		
		if type(self._key) is dict:  # a dictionary is returned if there is only one position, so convert it to list.
			self._key = [self._key]
		
		for position in self._key:
			new_position = Position(cost_basis=position['cost_basis'], date_acquired=position['date_acquired'],
			                        position_id=position['id'], quantity=position['quantity'],
			                        symbol=position['symbol'])
			
			positions.append(new_position)

		return positions
