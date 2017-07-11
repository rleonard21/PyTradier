Market Calendar
===============

.. autoclass:: pytradier.market.Calendar
    :members:
    :special-members:



Examples
~~~~~~~~

.. code-block:: python

    # Retrieve a dictionary of the market open intervals
    calendar = tradier.market.calendar()
    print calendar.open()  

The output is a dictionary with dates as keys and the status of the market on that particular date. Below is a shortened example output:

.. code-block:: python

   {u'2017-07-05': {u'start': u'09:30', u'end': u'16:00'}, u'2017-07-04': None, u'2017-07-03': {u'start': u'09:30', u'end': u'13:00'}}
  
The ``open()`` function (as well as ``premarket()`` and ``postmarket()``) returns a dictionary for each date in the main dictionary. This is useful since the information can be searched by its date (the key), or the entire dictionary can be looped through to get the values of each key. For example, to programmatically retrieve the market open interval from each day, use a ``for`` loop:

.. code-block:: python
   
    for key in calendar.open():
       print calendar.open()[key]  # loop through each nested dictionary
      
The (shortened) output of this is as follows:

.. code-block:: python

     None
     {u'start': u'09:30', u'end': u'16:00'}
     {u'start': u'09:30', u'end': u'16:00'}
