# You have to create a main course and a dessert at an Italian and
# a French restaurant, but you won't mix one cuisine with the other.
#
# Your task is:
#
# 1) define a class Product with an abstract method cook().
# This class would be base class for the next classes:
#
# - class FettuccineAlfredo with field name ("Fettuccine Alfredo"),
# method cook() provides an output of the formatted string "Italian main
# course prepared: " and name of the dish;
#
#  - class Tiramisu, with field name ("Tiramisu"), method cook() provides
#  an output of the formatted string "Italian dessert prepared:"
#  and name of the dish;
#
# - class DuckALOrange, with field name ("Duck À L'Orange"), method cook()
# provides an output of the formatted string "French main course
# prepared: " and name of the dish;
#
# - class CremeBrulee,  with field name ("Crème brûlée"), method cook()
# provides an output of the formatted string "French dessert
# prepared: " and name of the dish.
#
# 2) define a class Factory with an abstract method get_dish() that takes
# type_of_meal as a parameter. This class would be base class for
# the classes ItalianDishesFactory and FrenchDishesFactory.
# The method get_dish() according to type_of_meal ("main" or "dessert")
# invokes the dish of appropriate cousine;
#
# 3) define a class FactoryProducer with the method get_factory().
# The method takes the parameter type_of_factory and invokes
# the appropriate dishes factory (classes ItalianDishesFactory
# or FrenchDishesFactory).

# 1 step Product
class Product:
    def __init__(self):
        self.country = ""
        self.name = ""
        self.dish = ""

    def cook(self):
        print(f"{self.country} {self.dish} prepared: {self.name}")


class FettuccineAlfredo(Product):
    def __init__(self):
        super().__init__()
        self.name = "Fettuccine Alfredo"
        self.country = "Italian"
        self.dish = "main course"


class Tiramisu(Product):
    def __init__(self):
        super().__init__()
        self.name = "Tiramisu"
        self.country = "Italian"
        self.dish = "dessert"


class DuckALOrange(Product):
    def __init__(self):
        super().__init__()
        self.name = "Duck À L'Orange"
        self.country = "French"
        self.dish = "main course"


class CremeBrulee(Product):
    def __init__(self):
        super().__init__()
        self.name = "Crème brûlée"
        self.country = "French"
        self.dish = "dessert"


# 2 step Factory
class Factory:
    def __init__(self, *args):
        self.args = args

    def get_dish(self, type_of_meal):
        for x in self.args:
            if type_of_meal in x().dish:
                return x()


class ItalianDishesFactory(Factory):
    def __init__(self):
        super().__init__(FettuccineAlfredo, Tiramisu)
        self.country = "italian"


class FrenchDishesFactory(Factory):
    def __init__(self):
        super().__init__(DuckALOrange, CremeBrulee)
        self.country = "french"


# 3 FactoryProducer
class FactoryProducer:
    def __init__(self):
        self.args = (ItalianDishesFactory, FrenchDishesFactory)

    def get_factory(self, type_of_factory):
        for x in self.args:
            if x().country == type_of_factory:
                return x()
