---
title: Quotes
permalink: quotes.html
---
# Quotes
The `quote` class is the base class that both the `stock` class and `option` class inherit from. 
```
pytradier.securities.quote
```
# Stocks
Create an instance of the `stock` class using one or more symbols:
```python
tradier.stock(*symbols)
```

# Options
Create an instance of the `option` class using one or more symbols:
```python
tradier.option(*symbols)
```

## Methods
These are the methods accessible to both `stock` and `option`:
#
#
In addition to the above methods, the `options` class has a few additional functions specifically for options. 


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





