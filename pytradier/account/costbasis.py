class ClosedPosition:
    def __init__(self, close_date, open_date, term, cost, gl, gl_percent, proceeds, quantity, symbol):
	    self.close_date = close_date
	    self.open_date = open_date
	    self.term = term
	    self.cost = cost
	    self.gain_loss = gl
	    self.gain_loss_percent = gl_percent
	    self.proceeds = proceeds
	    self.quantity = quantity
	    self.symbol = symbol
