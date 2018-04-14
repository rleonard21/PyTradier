class Order:
	def __init__(self, order_id=None, order_type=None, symbol=None, side=None, quantity=None, status=None,
				duration=None, price=None, avg_fill_price=None, exec_quantity=None, last_fill_price=None,
                last_fill_quantity=None, remaining_quantity=None, create_date=None, transaction_date=None,
	            class_type=None):

		self.id = order_id
		self.type = order_type
		self.symbol = symbol
		self.side = side
		self.quantity = quantity
		self.status = status
		self.duration = duration
		self.price = price
		self.avg_fill_price = avg_fill_price
		self.exec_quantity = exec_quantity
		self.last_fill_price = last_fill_price
		self.last_fill_quantity = last_fill_quantity
		self.remaining_quantity = remaining_quantity
		self.create_date = create_date
		self.transaction_date = transaction_date
		self.class_type = class_type
