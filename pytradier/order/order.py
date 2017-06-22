class Order:
    def __init__(self):
        pass

    def create(self, _class, duration, side, quantity, _type, price=None, stop=None,
               option_symbol=None, symbol=None, preview=False ):

        if symbol is None and option_symbol is None:
            # Raise an error because both symbols are not defined
            pass




        pass

    def create_multi(self):
        pass

    def change(self):
        pass

    def cancel(self):
        pass
