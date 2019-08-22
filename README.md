# ShoppingCart

# General 
Python Shopping Cart example

Simple shopping cart emulator incorprating discounts and special offers.

# Simple cart example
  import ShoppingCart as CART

  cart = CART.ShoppingCart()
  cart.addItems('Baked Beans', 2) # 1.98
  cart.addItems('Biscuits', 1)    # 1.20
  cart.addItems('Sardines', 2)    # 2 Sardines@1.89 == price: 3.78 disc: 0.95
  cart.display()
  subtot, disc, tot = cart.getTotal()  # returns sub-total: 6.96 discounts: 0.95 total: 6,01


# To run the tests:

  python ShoppingCartTests.py
  
# TODO

  

