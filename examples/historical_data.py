from pytradier.tradier import Tradier

# Authenticate with the API. Historical data requires a brokerage account.
tradier = Tradier(token='YourToken', account_id='YourAccountID', endpoint='brokerage')

# historical prices come from the Company class. choose which company's data to model:
company = tradier.company(symbol='AAPL')

# get the historical prices between 2011 and 2012
history = company.history(interval='monthly', start='2011-1-1', end='2012-1-1')

# you can now use the history object to retrieve data associated with a specific date. each method returns a dictionary
# with a date as the key and the data as the value. for example:
print('Opening price of AAPL for 2011-2012:')
print(history.open())

# if you need a list instead of a dictionary, the bundle method returns a sorted list of all pieces of data associated
# with each day. returns list in the form [epoch, open, close, high, low, volume]. if the reverse_sort option is
# enabled, the data is sorted from newest to oldest. for example:
raw_data = history.bundle(reverse_sort=True)
print('\nAll data for AAPL in 2011-2012:')
print(raw_data)

# the bundle data can be accessed just like any python list:
print('\nThe most recent data in the interval:')
print('Timestamp: {}, Opening price: {}, closing price: {}, High: {}, Low: {}, Volume: {}'.format(
	raw_data[0][0], raw_data[0][1], raw_data[0][2], raw_data[0][3], raw_data[0][4], raw_data[0][5]))
