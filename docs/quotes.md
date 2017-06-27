---
title: Quotes
permalink: quotes.html
---
# Quotes
The `stock` and `option` classes inherit from the `quote` class. 
```
pytradier.securities.quote
```
## Stocks
Create an instance of the `stock` class using one or more symbols:
```python
tradier.stock(*symbols)
```

## Options
Create an instance of the `option` class using one or more symbols:
```python
tradier.option(*symbols)
```

## Methods
These are the methods accessible to both `stock` and `option`.
Each function is set to update from the API by default. To prevent the program from calling Tradier's API (to preserve call limits), set the `update` parameter to false. 

###### `symbol()`	
Symbol, e.g. `AAPL`, `MSFT`, etc.

###### `desc(update=True)`
Symbol description.

###### `exch(update=True)`
Exchange the symbol is sold on.

###### `type(update=True)`	
Type of security (i.e. stock, etf, option, index)

###### `change(update=True)`
Daily net change

###### `change_percentage(update=True)`
Daily net change in percent

###### `volume(update=True)`	
Volume for the day

###### `average_volume(update=True)`
Average daily volume

###### `last_volume(update=True)`
Last incremental volume

###### `trade_date(update=True)`
Date and time of last trade

###### `open(update=True)`
Opening price

###### `high(update=True)`
Trading day high

###### `low(update=True)`
Trading day low

###### `close(update=True)`
Closing price

###### `prevclose(update=True)`
Previous closing price

###### `week_52_high(update=True)`
52 week high

###### `week_52_low(update=True)`
52 week low

###### `bid(update=True)`
Current bid

###### `bidsize(update=True)`
Size of bid

###### `bidexch(update=True)`
Exchange of bid

###### `bid_date(update=True)`
Date and time of current bid

###### `ask(update=True)`
Current ask

###### `asksize(update=True)`
Size of ask

###### `askexch(update=True)`
Exchange of ask

###### `ask_date(update=True)`
Date and time of current ask


##### Additional `option` Methods
In addition to the above methods, the `option` class has a few additional functions specifically for options. 

###### `strike()`
Returns the saved strike price of the option

###### `expiration()`
Returns the expiration date of the contract, in the format YYY-MM-DD

###### `expiration_type()`
Returns the type of expiration. For example, `weeklys` or `monthlys`.

###### `option_type()`
The type of option, `put` or `call`. 

###### `contract_size()`
Size of the contract in shares.

###### `underlying()`
Returns the underlying symbol(s).

###### `open_interest()`
Open interest for the contract.

## Example Code
```python
# Initialize Tradier
tradier = Tradier(token='abc123', account_id=None, endpoint=None)

# You can place multiple symbols in the call
stocks = tradier.stock('AAPL', 'MSFT', 'GOOG')

# Call a method of the stock class
stocks.bid()
```
The output is a dictionary and should look similar to this:
```python
{AAPL: 145.93, MSFT: 70.11, GOOG: 944.01}
```




