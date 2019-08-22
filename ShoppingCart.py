#
# ShopppingCart.py
#
# Shopping Cart emulator
# 
# Chris Folan Aug 2019
#

from collections import defaultdict
from collections import namedtuple
from functools import reduce
import  math

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

# Catalogue / Price list
# For test purposes I have simply hardwired it - TODO - make catalogue configurable
catalogue = {}
catalogue['Baked Beans'] = 0.99
catalogue['Biscuits'] = 1.20
catalogue['Sardines'] = 1.89
catalogue['Shampoo (Small)'] = 2.00
catalogue['Shampoo (Medium)'] = 2.50
catalogue['Shampoo (Large)'] = 3.50

# Discount
# For test purposes I have simply hardwired the discount - TODO - make discounts configurable

# Point = namedtuple('Point', 'x y')
Discount_Bogof      = namedtuple('Bogof', 'num free')
Discount_Percentage = namedtuple('Percentage', 'perc')

discounts = {}
discounts['Baked Beans'] = Discount_Bogof(2,1)
discounts['Sardines']    = Discount_Percentage(25)

# Bonus Question 2
'''
Under some circumstances multiple discounts may be applicable to a single product.
For example:
"Buy any 3 of Shampoo (Small), Shampoo (Medium) and Shampoo (Large), and you get the cheapest one for free.
Shampoo Medium is 50% off
When determining which product is "cheapest", other discounts may apply.
'''
special_offers_cheapest_free = (['Shampoo (Small)', 'Shampoo (Medium)', 'Shampoo (Large)'], 3)
special_discounts = {}
special_discounts['Shampoo (Medium)']    = 50   # 50% off - TBC - inconsistent with previous discounts...
special_discounts['Shampoo (Medium)']    = 50   # 50% off - TBC - inconsistent with previous discounts...


def round_up(n, decimals=0):
    '''
    round up function to get around python rounding issue  0.945 => round up 2dp == 0.95 (normal python round ==> 0.94)
    '''
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier

class ShoppingCart():
    def __init__(self):
        self._basket = defaultdict(int)

    def addItem(self, item, qty=1):
        self._basket[item] += qty       # Baked Beans / 3 tins

    def addItems(self, item, qty = 1):
        self.addItem(item,qty)

    def howMany(self, item):
        return self._basket[item]

    def getTotalItems(self):
        return reduce(lambda x,y: x+y, self._basket.values())

    def getDiscount(self, discount, qty, price):
        '''
            Baked Beans: buy 2 get 1 free
            Sardines: 25% discount
        '''
        disc = 0

        if type(discount) == (Discount_Bogof):
            '''
                Baked Beans: buy 2 get 1 free
                eg. but 7 tins == 2 free (for every 3 tins you buy 1 is free)
            '''
            numFree = qty // (discount.num + discount.free)
            disc = numFree * price
            print ("Discount_Bogof num free: {}".format(numFree))

        elif type(discount) == (Discount_Percentage):
            '''
                Sardines: 25% discount
            '''
            print ("Discount_Percentage")
            perc = discount.perc / 100
            disc = qty * price * perc   # 2 Sardines @ 1.89 = 3.78 * 25% = 0.95

        return round_up(disc,2)

    def getTotal(self, special_offers = False):
        '''
            sum up the basket - applyiong discounts where necessary 
            return sub-total, discount, total
        '''
        tot = 0
        tot_disc = 0
        so_disc = 0

        if special_offers:
            so_disc = self.getSpecialOffersDiscount()       # TODO - this should be integrated with other discounts

        for item,qty in self._basket.items():
            # get sub price
            disc = 0
            sub_price = catalogue[item] * qty

            # get discount
            discount = discounts.get(item,None)
            if discount:
                print ("item: {} discount: {}".format(item,discount))
                disc = self.getDiscount(discount,qty,catalogue[item])

            print ("item: {} quantity: {} price: {} disc: {} so_disc: {}".format(item, qty, sub_price, disc, so_disc) )
            tot_disc += disc
            tot_disc += so_disc     # special offers
            tot      += sub_price
        return round_up(tot,2), round_up(tot_disc,2), round_up((tot - tot_disc),2)  # return sub-total, discount, total

    def updateCatalogue(self):
        '''
        apply special offers to catalogue  - TBC completed
        '''
        for item,perc in special_discounts.items():
            price_before = catalogue[item]
            price_after  = price_before * (perc/100)
            catalogue[item] = price_after
            print ("updateCatalogue {} {} => {} ".format(item, price_before, price_after))

    def getSpecialOffersDiscount(self):
        '''
        crude function to calculate the special offer
        eg. Buy any 3 of Shampoo (Small), Shampoo (Medium) and Shampoo (Large), and you get the cheapest one for free.
        '''
        disc = 0
        self.updateCatalogue()      # apply special offers to catalogue
        tot_so = 0
        so_prices = []
        print ("applying special offers")
        special_offers = special_offers_cheapest_free[0]        # shampoo S / M / L
        num_must_buy   = special_offers_cheapest_free[1]        # must buy 3
        for so in special_offers:
            tot = self.howMany(so)  # Shampoo (Small) == 5
            # update list of prices of the special offers
            so_prices += ([catalogue[so]] * tot)                 # 2.00 2.00 2.00 2.00 2.00  - crude way of picking the 3 cheapest later
            tot_so += tot                                   # sum up special offers bought
            print (so, tot)

        if tot_so >= num_must_buy:
            num_eligible = tot_so // num_must_buy           # you must buy 3 to be eligible - so if you buy 10 you are eligible for 3 free (cheapest)
            disc = sum(sorted(so_prices)[:num_must_buy])    # sum up the 3 cheapest
            print ("purchased {} specials - so eligible for {} cheapest specials {} => {}".format(tot_so, num_eligible, sorted(so_prices), disc))

        return disc


    def display(self):
        for item,qty in self._basket.items():
            print ("item: {} quantity: {}".format(item,qty) )



def applyOffers(basket):
    sub, disc = 5.16, 0.99
    tot = sub - disc
    return sub , disc, tot

if __name__ == "__main__":
    main()

