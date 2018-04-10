from pytradier.tradier import Tradier

# authenticate with the Tradier API
tradier = Tradier(token='YourToken', account_id='YourAccountID', endpoint='brokerage')

# create an instance of the stock class with a few companies
stocks = tradier.stock('AAPL', 'MSFT')

# and print the current ask price:
print(stocks.ask())

# you can always add more stocks to this instance:
stocks.add_symbols('FB', 'NFLX')

# and print current bid price to show the updated stocks:
print(stocks.bid())

# you can now use any of the methods associated with the Stock class!
