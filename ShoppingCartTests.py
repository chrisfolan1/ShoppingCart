#
# ShopppingCartTests.py
#
# simple unit tests for the ShoppingCart
#
'''
Catalogue
    Baked Beans £0.99
    Biscuits £1.20
    Sardines £1.89
    Shampoo (Small) £2.00
    Shampoo (Medium) £2.50
    Shampoo (Large) £3.50
Offers
    Baked Beans: buy 2 get 1 free
    Sardines: 25% discount
'''

import ShoppingCart as CART
import unittest


class TestShoppingCart(unittest.TestCase):

    def test_basket(self):
        '''
        test simple basket with offer...

        Baked Beans x 4
        Biscuits x 1
        Should give the results:
            sub-total: £5.16
            discount: £0.99
            total: £4.17
        '''
        b1 = { 'Baked Beans':2, 'Biscuits': 1 }
        sub, disc, tot = CART.applyOffers(b1)
        self.assertEqual(tot, 4.17)

    def test_add_items_total_specific_item(self):
        ''' add some items - check number of a specific item '''
        cart = CART.ShoppingCart()
        cart.addItems('Baked Beans', 4)
        cart.addItem('Baked Beans')
        cart.addItems('Baked Beans', 2)
        cart.addItems('Shampoo (Large)', 2)
        numBB = cart.howMany('Baked Beans')
        cart.display()
        self.assertEqual(numBB, 7)

    def test_tot_items(self):
        ''' add some items - check total num items '''
        cart = CART.ShoppingCart()
        cart.addItems('Baked Beans', 4)
        cart.addItems('Baked Beans', 2)
        cart.addItems('Biscuits', 10)
        cart.addItem('Baked Beans')
        cart.addItems('Shampoo (Large)', 2)
        self.assertEqual(cart.getTotalItems(), 19)


    def test_tot1(self):
        ''' add a range of items (with offers) and check totals at end '''
        cart = CART.ShoppingCart()
        cart.addItems('Baked Beans', 4)
        cart.addItems('Baked Beans', 2)
        cart.addItems('Biscuits', 10)           # 10 Biscuits@1.20 == 12.00
        cart.addItems('Sardines', 2)            # 2 Sardines@1.89 == price: 3.78 disc: 0.95
        cart.addItem('Baked Beans')             # 7 Beans@0.99 == 2 free -  price: 6.93 disc: 1.98
        cart.addItems('Shampoo (Large)', 2)     # 2 Shampoo @ 3.50 == 7.00

        subtot, disc, tot = cart.getTotal()
        self.assertEqual(subtot, 29.71)
        self.assertEqual(disc, 2.93)
        self.assertEqual(tot, 26.78)

    def test_tot2(self):
        '''
            add a range of items (with offers) and check totals at end

            Baked Beans x 2
            Biscuits x 1
            Sardines x 2

            sub-total: £6.96
            discount: £0.95
            total: £6.01
        '''
        cart = CART.ShoppingCart()
        cart.addItems('Baked Beans', 2) # 1.98
        cart.addItems('Biscuits', 1)    # 1.20
        cart.addItems('Sardines', 2)    # 2 Sardines@1.89 == price: 3.78 disc: 0.95
        cart.display()
        subtot, disc, tot = cart.getTotal()
        self.assertEqual(subtot, 6.96)
        self.assertEqual(disc, 0.95)
        self.assertEqual(tot, 6.01)


    def test_tot2(self):
        '''
        Baked Beans x 4
        Biscuits x 1
        Should give the results:

        sub-total: £5.16
        discount: £0.99
        total: £4.17
        '''
        cart = CART.ShoppingCart()
        cart.addItems('Baked Beans', 4) # 3.96 (1 free)
        cart.addItems('Biscuits', 1)    # 1.20
        subtot, disc, tot = cart.getTotal()
        self.assertEqual(subtot, 5.16)
        self.assertEqual(disc, 0.99)
        self.assertEqual(tot, 4.17)

    def test_special_offers(self):
        '''
        Bonus question 2
        eg. Buy any 3 of Shampoo (Small), Shampoo (Medium) and Shampoo (Large), and you get the cheapest one for free.

        '''
        cart = CART.ShoppingCart()
        cart.addItems('Baked Beans', 1) 
        cart.addItems('Shampoo (Small)',  5)
        cart.addItems('Shampoo (Medium)', 1)
        cart.addItems('Shampoo (Large)',  4)

        subtot, disc, tot = cart.getTotal(special_offers = True)

        self.assertEqual(subtot, 26.24)
        self.assertEqual(disc, 21.00)
        self.assertTrue(tot in [5.24,5.25]) # ouch - TBC - fix python rounding 



if __name__ == '__main__':
    unittest.main()


