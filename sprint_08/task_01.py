# Write the programm that calculate total price with discount by
# the products.
#
# Use class Product(name, price, count) and class Cart. In class
# Cart you can add the products.
#
# Discount depends on count product:
#
#
# count	discount
# at least 5	5%
# at least 7	10%
# at least 10	20%
# at least 20	30%
# more than 20	50%
# Write unittest with class CartTest and test all methods with logic

import unittest


class Product:
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count


class Cart:
    def __init__(self, *args):
        self.products = args

    def get_total_price(self):
        res = []
        for prod in self.products[0]:
            count = prod.count
            price = prod.price
            if count > 20:
                res.append((price * 0.5) * count)
            elif count == 20:
                res.append((price * 0.7) * count)
            elif count >= 10:
                res.append((price * 0.8) * count)
            elif count >= 7:
                res.append((price * 0.9) * count)
            elif count >= 5:
                res.append((price * 0.95) * count)
            else:
                res.append((price * count))
        return sum(res)


class CartTest(unittest.TestCase):
    def setUp(self) -> None:
        self.products = (Product('p1', 10, 4),
                    Product('p2', 100, 5),
                    Product('p3', 200, 6),
                    Product('p4', 300, 7),
                    Product('p5', 400, 9),
                    Product('p6', 500, 10),
                    Product('p7', 1000, 20))

        self.zero_products = (Product('p1', 0, 0),
                         Product('p2', 0, 0),
                         Product('p3', 0, 0),
                         Product('p4', 0, 0),
                         Product('p5', 0, 0),
                         Product('p6', 0, 0),
                         Product('p7', 0, 0))

        self.with_type_error_products = Product('p1', "", 0)

        self.cart = Cart(self.products)
        self.cart_zero = Cart(self.zero_products)
        self.error_cart = Cart(self.with_type_error_products)

    def test_cart_total_with_discounts_equal(self):
        self.assertEqual(self.cart.get_total_price(), 24785.0)

    def test_cart_total_with_discounts_equal_zero(self):
        self.assertEqual(self.cart_zero.get_total_price(), 0)

    def test_cart_with_type_error_product(self):
        with self.assertRaises(TypeError):
            self.error_cart.get_total_price()
