Market Calendar
===============

.. autoclass:: pytradier.market.Calendar
    :members:




.. code-block:: python

   calendar = tradier.market.calendar()
   print calendar.status()  

The output is a dictionary with dates as keys and the status of the market on that particular date. Below is a shortened example output:

.. code-block:: python

   {u'2017-07-05': u'open', u'2017-07-04': u'closed'}
