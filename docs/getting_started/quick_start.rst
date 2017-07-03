Quick Start
===========

PyTradier first needs to have the ``Tradier`` class initialized, which is how the program logs into the API. This is required since all of Tradier's API is private and requires authentication before accessing. This can be done using the following example:


.. code-block:: python

 import PyTradier

 tradier = Tradier(token='abc123', account_id='123456', sandbox=False)

The initialization for ``Tradier`` takes three parameters:

* ``token`` Your API access token provided by Tradier. *Required.*
* ``account_id`` The ID number associated with your Tradier Brokerage account. You will only have this if you have opened a Brokerage account with Tradier. *Optional.*
* ``sandbox`` Determines whether the sandbox or full API endpoint will be used. Sandbox has limited access, but it completely free. The full API requires a Brokerage account. *Optional.*

Once the ``Tradier`` class has been initialized, all submodules can be called like this:

.. code-block:: python

 stocks = tradier.stock('AAPL', 'MSFT')
 options = tradier.option('AAPL170630P00130000')










