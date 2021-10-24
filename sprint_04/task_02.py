# Create a Pizza class with the attributes order_number and ingredients
# (which is given as a list). Only the ingredients will be given as input.
#
# You should also make it so that its possible to choose a ready made
# pizza flavour rather than typing out the ingredients manually!
# As well as creating this Pizza class, hard-code the following pizza
# flavours.
#

# Examples:
# p1 = Pizza(["bacon", "parmesan", "ham"])   # order 1
# p2 = Pizza.garden_feast()                  # order 2
# p1.ingredients ➞ ["bacon", "parmesan", "ham"]
# p2.ingredients ➞ ["spinach", "olives", "mushroom"]
# p1.order_number ➞ 1
# p2.order_number ➞ 2

pizzas = {
    "hawaiian": ["ham", "pineapple"],
    "meat_festival": ["beef", "meatball", "bacon"],
    "garden_feast": ["spinach", "olives", "mushroom"]
}

class Pizza:
    orders_list = []
    _pizzas = pizzas

    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.orders_list.append(ingredients)
        self.order_number = self.orders_list.index(self.ingredients) + 1

    @classmethod
    def garden_feast(cls):
        ingredients = cls._pizzas.get("garden_feast")
        return cls(ingredients)

    @classmethod
    def hawaiian(cls):
        ingredients = cls._pizzas.get("hawaiian")
        return cls(ingredients)

    @classmethod
    def meat_festival(cls):
        ingredients = cls._pizzas.get("meat_festival")
        return cls(ingredients)

