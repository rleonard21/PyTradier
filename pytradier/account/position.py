class Position:
	def __init__(self, cost_basis, date_acquired, position_id, quantity, symbol):
		self.cost_basis = cost_basis
		self.date_acquired = date_acquired
		self.id = position_id
		self.quantity = quantity
		self.symbol = symbol
