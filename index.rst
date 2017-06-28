======
Quotes
======

Quotes
======

The ``quote`` class is the base class that both the ``stock`` class and
``option`` class inherit from.

::

    pytradier.securities.quote

Stocks
======

Create an instance of the ``stock`` class using one or more symbols:

.. code:: python

    tradier.stock(*symbols)

Options
=======

Create an instance of the ``option`` class using one or more symbols:

.. code:: python

    tradier.option(*symbols)

Methods
-------

These are the methods accessible to both ``stock`` and ``option``: # #
In addition to the above methods, the ``options`` class has a few
additional functions specifically for options.

``strike(update=False)``      Returns the saved strike price

``expiration()``      Returns the saved strike price
