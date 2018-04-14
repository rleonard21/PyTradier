from ..base import Base
from .events import Trade, Journal, DIVADJ, STKMVE
from ..const import API_PATH
import os


class History(Base):
	def __init__(self, limit=25):
		Base.__init__(self)
		
		self._path = API_PATH['account_history'].replace('{account_id}', os.environ['API_ACCOUNT_ID'])
		self._path += '?limit={}'.format(limit)
		self._data = self._api_response(endpoint=self._endpoint, path=self._path, payload=self._payload)
		self._key = self._data['history']['event']
		self._inner_key = 'type'
		
		self.trades = []
		self.journal = []
		self.div_adjs = []
		self.stock_moves = []

		for event in self._key:
			if event['type'] == 'trade':
				t = event['trade']
				new_event = Trade(amount=event['amount'], date=event['date'], event_type=event['type'],
				                  comm=t['commission'], desc=t['description'], price=t['price'], quantity=t['quantity'],
				                  symbol=t['symbol'], trade_type=t['trade_type'])
				
				self.trades.append(new_event)
			
			if event['type'] == 'journal':
				t = event['journal']
				new_event = Journal(amount=event['amount'], date=event['date'], event_type=event['type'],
				                    desc=t['description'], quantity=t['quantity'])
				
				self.journal.append(new_event)
			
			if event['type'] == 'DIVADJ':
				t = event['adjustment']
				new_event = DIVADJ(amount=event['amount'], date=event['date'], event_type=event['type'],
				                   desc=t['description'], quantity=t['quantity'])
				
				self.div_adjs.append(new_event)
			
			if event['type'] == 'STKMVE':
				t = event['adjustment']
				new_event = STKMVE(amount=event['amount'], date=event['date'], event_type=event['type'],
				                   desc=t['description'], quantity=t['quantity'])
				
				self.stock_moves.append(new_event)
