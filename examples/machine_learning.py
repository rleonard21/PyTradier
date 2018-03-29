from sklearn import svm
import numpy as np

from pytradier.tradier import Tradier

'''
The purpose of this example is to show the user how to use the PyTradier library in conjunction with scikit-learn
for machine learning. This example takes training data from PyTradier, trains an SVM classifier with arbitrary labels,
then predicts a buy or sell action for an arbitrary time and price. 

Note... The labels for the training data in this example are arbitrary (i.e. random), so there isn't any connection
between the labels and the data. Due to this, this example is unlikely to be accurate in predicting a buy/sell action.
'''

# Authenticate with the API. Historical data requires a brokerage account.
tradier = Tradier(token='YourToken', account_id='YourAccountID', endpoint='brokerage')

# choose which company's data to model
company = tradier.company(symbol='AAPL')

# get the historical prices between 2011 and 2012
history = company.history(interval='monthly', start='2011-1-1', end='2012-1-1')
raw_data = history.bundle(reverse_sort=True)  # returns list in the form [epoch, open, close, high, low, volume]

# convert the data to a numpy array
data_arr = np.array(raw_data, dtype='float64')

# create an array in the form [epoch, open]
parsed_data = data_arr[:, 0:2]

# an example list of labels for each datapoint, with a 0 representing sell and 1 representing buy.
# These labels should be determined using external financial indicators such as ADX, MFI, MACD, etc.
labels = [1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0]

# create an SVM classifier
clf = svm.SVC()
clf.fit(parsed_data, labels)

# predict the classification of an arbitrary point (in the format [epoch, price])
prediction = clf.predict([[1.29385800e+09, 1]])

if prediction == 1:
	print('Buy')

else:
	print('sell')
