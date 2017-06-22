from . import models

class Option:
    def chain(self, symbol, expiration):
        return models.option.Chain(symbol, expiration)

    def strike(self, symbol, expiration):
        return models.option.Strike(symbol, expiration)

    def expiration(self, symbol):
        return models.option.Expiration(symbol)