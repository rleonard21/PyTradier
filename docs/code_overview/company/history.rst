Historical Pricing
==================

.. autoclass:: pytradier.company.History
  :special-members:
  :members:

Examples
~~~~~~~~
A year's worth of historical prices can be retrieved using this example:

.. code-block:: python

  company = tradier.company(symbol='AAPL')
  history = company.history(interval='daily', start='2011-1-1', end='2012-1-1')
  print history.high()
