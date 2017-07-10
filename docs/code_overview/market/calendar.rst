Market Calendar
===============

A class for obtaining information about the market, including searching for companies and the market status. 

.. note::
   The output of each method is a dictionary with a date as the key and the particular value of the method as the value.

.. autoclass:: pytradier.market.Calendar
    :members:


Examples
========

.. code-block:: python

   calendar = tradier.market.calendar()
   print calendar.status()  

The output is a dictionary with dates as keys and the status of the market on that particular date. Below is a shortened example output:

.. code-block:: python

   {u'2017-07-05': u'open', u'2017-07-04': u'closed'}
