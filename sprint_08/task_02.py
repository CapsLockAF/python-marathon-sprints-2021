# Please, write the code with unit tests for the function "divide":
# minimum 3 tests
# must chek all flows
# all test must be pass
# no failures
# no skip
import unittest
from parameterized import parameterized


def divide(num_1, num_2):
    return float(num_1)/num_2


class DivideTest(unittest.TestCase):

    def test_positive_divide(self):
        self.assertEqual(divide(6, 2), 3.0)

    def test_string_to_float_num_1(self):
        self.assertEqual(divide("6", 2), 3.0)

    def test_positive_divide_almost(self):
        actual = divide(1, 3)
        expected = 0.333333
        self.assertAlmostEqual(actual, expected, 6)

    def test_is_negative_divide(self):
        self.assertLess(divide(-5, 10), 0)

    def test_zero_division_error(self):
        self.assertRaises(ZeroDivisionError, divide, 3, 0)

    def test_missed_arguments_type_error(self):
        with self.assertRaises(TypeError):
            divide()

    def test_wrong_arguments_type_error(self):
        with self.assertRaises(Exception):
            divide("f", 5)


