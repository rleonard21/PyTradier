from pytradier.tradier import Tradier

# authenticate with the Tradier API
tradier = Tradier(token='YourToken', account_id='YourAccountID', endpoint='brokerage')

# the options chain comes from the Company class, since the options chain is associated with a particular company.
# first create an instance of the Company class:
company = tradier.company(symbol='AAPL')

# the chain can be accessed like this: (note, the supplied expiration date must be a friday!)
chain = company.chain(expiration='2018-04-13')

# the chain will return a dictionary of each expiration. To see the strike price of each option, for example:
print('Complete options chain with strike price:')
print(chain.strike())

# note that the key of each element in the dictionary is the symbol for the option itself. the symbol for the option
# can also be retrieved using the Symbol method:
print('\nOptions chain with symbols:')
print(chain.symbol())

# this method will be useful for the next step, so let's grab the first two options in the dictionary an an example:
my_option_1 = list(chain.symbol())[0]
my_option_2 = list(chain.symbol())[1]

# to track specific options instead of the chain, use the Option class. You can pass in as many options symbols
# as you want:
options = tradier.option(my_option_1, my_option_2)

# now we can retrieve the ask price for the two options we picked above:
print('\nOptions class with ask price:')
print(options.ask())

# you can now use any of the methods available to the Options class to retrieve information about specific options!
