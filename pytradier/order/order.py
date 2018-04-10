class Order:
    def __init__(self):
        pass

    def create(self, _class, duration, side, quantity, _type, price=None, stop=None,
               option_symbol=None, symbol=None, preview=False ):

        if symbol is None and option_symbol is None or \
            symbol is not None and option_symbol is not None:
            # If the user provides both a symbol and option_symbol, through exception

            raise TypeError('Either `symbol` or `option_symbol` must be provided, but not both')







        pass

    def create_multi(self):
        pass

    def change(self):
        pass

    def cancel(self):
        pass
