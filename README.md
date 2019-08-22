# ShoppingCart

# General 
Python Shopping Cart example

Simple shopping cart emulator incorprating discounts and special offers.

# Simple cart example
```python
  import ShoppingCart as CART

  cart = CART.ShoppingCart()
  cart.addItems('Baked Beans', 2) # 1.98
  cart.addItems('Biscuits', 1)    # 1.20
  cart.addItems('Sardines', 2)    # 2 Sardines@1.89 == price: 3.78 disc: 0.95
  cart.display()
  subtot, disc, tot = cart.getTotal()  # returns sub-total: 6.96 discounts: 0.95 total: 6,01
```

# To run the tests:

  *python ShoppingCartTests.py*
  
# TODO

  The present version of the code has the Catalogue and Discounts hard-wired in the main scipt.
  Future versions will have these as separate configurable modules.
  
  The *test_special_offers()* test method is written to support "Bonus Question 2"
  -- Buy any 3 of Shampoo (Small), Shampoo (Medium) and Shampoo (Large), and you get the cheapest one for free.
  
  The *special_offers* flag is used to trigger whether the special offers are to be applied or not:
  ```python
          subtot, disc, tot = cart.getTotal(special_offers = True)
  ```
  


