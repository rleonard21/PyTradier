class Event:
    def __init__(self, amount, date, event_type):
	    
	    self.amount = amount
	    self.date = date
	    self.event_type = event_type


class Trade(Event):
	def __init__(self, amount, date, event_type, comm, desc, price, quantity, symbol, trade_type):
		Event.__init__(self, amount, date, event_type)
		
		self.total_cost = self.amount
		self.commission = comm
		self.desc = desc
		self.buy_price = price
		self.quantity = quantity
		self.symbol = symbol
		self.trade_type = trade_type


class Journal(Event):
	def __init__(self, amount, date, event_type, desc, quantity):
		Event.__init__(self, amount, date, event_type)
		
		self.desc = desc
		self.quantity = quantity


class DIVADJ(Journal):
	def __init__(self, amount, date, event_type, desc, quantity):
		Journal.__init__(self, amount, date, event_type, desc, quantity)


class STKMVE(Journal):
	def __init__(self, amount, date, event_type, desc, quantity):
		Journal.__init__(self, amount, date, event_type, desc, quantity)
