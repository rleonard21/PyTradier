Quotes
======

The ``stock`` and ``option`` classes inherit from the ``quote`` class.

::

    pytradier.securities.quote

Stocks
------

Create an instance of the ``stock`` class using one or more symbols:

.. code:: python

    tradier.stock(*symbols)

Options
-------

Create an instance of the ``option`` class using one or more symbols:

.. code:: python

    tradier.option(*symbols)

Methods
-------

These are the methods accessible to both ``stock`` and ``option``. Each
function is set to update from the API by default. To prevent the
program from calling Tradier's API (to preserve call limits), set the
``update`` parameter to false.

``update()``
            

Updates the information for all symbols listed in the instance.

``add_symbols(*symbols)``
                         

Add a symbol to the instance of the class. Can take multiple symbols.

``symbol()``
            

Symbol, e.g. ``AAPL``, ``MSFT``, etc.

``desc(update=True)``
                     

Symbol description.

``exch(update=True)``
                     

Exchange the symbol is sold on.

``type(update=True)``
                     

Type of security (i.e. stock, etf, option, index)

``change(update=True)``
                       

Daily net change

``change_percentage(update=True)``
                                  

Daily net change in percent

``volume(update=True)``
                       

Volume for the day

``average_volume(update=True)``
                               

Average daily volume

``last_volume(update=True)``
                            

Last incremental volume

``trade_date(update=True)``
                           

Date and time of last trade

``open(update=True)``
                     

Opening price

``high(update=True)``
                     

Trading day high

``low(update=True)``
                    

Trading day low

``close(update=True)``
                      

Closing price

``prevclose(update=True)``
                          

Previous closing price

``week_52_high(update=True)``
                             

52 week high

``week_52_low(update=True)``
                            

52 week low

``bid(update=True)``
                    

Current bid

``bidsize(update=True)``
                        

Size of bid

``bidexch(update=True)``
                        

Exchange of bid

``bid_date(update=True)``
                         

Date and time of current bid

``ask(update=True)``
                    

Current ask

``asksize(update=True)``
                        

Size of ask

``askexch(update=True)``
                        

Exchange of ask

``ask_date(update=True)``
                         

Date and time of current ask

Additional ``option`` Methods
'''''''''''''''''''''''''''''

In addition to the above methods, the ``option`` class has a few
additional functions specifically for options.

``strike()``
            

Returns the saved strike price of the option

``expiration()``
                

Returns the expiration date of the contract, in the format YYY-MM-DD

``expiration_type()``
                     

Returns the type of expiration. For example, ``weeklys`` or
``monthlys``.

``option_type()``
                 

The type of option, ``put`` or ``call``.

``contract_size()``
                   

Size of the contract in shares.

``underlying()``
                

Returns the underlying symbol(s).

``open_interest()``
                   

Open interest for the contract.

Example Code
============

Getting started
##############

All programs will need to initalize the PyTradier class by first calling
the ``Tradier`` class.

.. code:: python

    # Initialize Tradier
    tradier = Tradier(token='abc123', account_id=None, endpoint=None)

    # You can place multiple symbols in the call
    stocks = tradier.stock('AAPL', 'MSFT', 'GOOG')

    # Call a method of the stock class
    print stocks.bid()

The output is a dictionary and should look similar to this:

.. code:: python

    {AAPL: 145.93, MSFT: 70.11, GOOG: 944.01}

Adding symbols
##############

.. code:: python

    # add two symbols to the instance but do not update
    stocks.add_symbol('AMZN', 'NFLX', update=False)
    print stocks.symbol()

Since we set ``update=False``, the library does not access the Tradier
API until the update function is called. Thus, the ouput only contains
the symbols as before:

.. code:: python

    {AAPL: AAPL, MSFT: MSFT, GOOG: GOOG}

To update the stocks, calling the ``update`` method will fetch the most
up-to-date information from the API:

.. code:: python

    stocks.update()
    print stocks.symbol()

.. code:: python

    # output
    {AAPL: AAPL, MSFT: MSFT, GOOG: GOOG, AMZN: AMZN, NFLX: NFLX}

By setting ``update=False``, you have more control over when your script
calls the API for new information, therefore giving you control over the
API limit rates. Otherwise, ``update=True`` is default to give you the
most up to date information.
