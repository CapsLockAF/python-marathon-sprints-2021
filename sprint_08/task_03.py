# Write th function quadratic_equation with arguments a, b ,c that solution
# to quadratic equation without a complex solution.
#
# Write unit tests for this function with QuadraticEquationTest class
#
# Minimum 3 tests: discriminant < 0, discriminant > 0, discriminant = 0
import unittest


def quadratic_equation(a, b, c):
    if a == 0:
        raise ValueError
    # calculate the discriminant
    d = (b ** 2) - (4 * a * c)
    x1 = (-b + (d ** 0.5)) / (2 * a)
    x2 = (-b - (d ** 0.5)) / (2 * a)
    if d > 0:
        return x1, x2
    elif d == 0:
        return x1
    else:
        return None


class QuadraticEquationTest(unittest.TestCase):
    def test_discriminant_is_negative(self):
        self.assertEqual(quadratic_equation(5, 2, 3), None)

    def test_discriminant_is_positive(self):
        self.assertEqual(quadratic_equation(5, 2, -3), (0.6, -1.0))

    def test_discriminant_is_zero(self):
        self.assertEqual(quadratic_equation(1, -4, 4), 2.0)

    def test_a_zero_raised_value_error(self):
        with self.assertRaises(ValueError):
            quadratic_equation(0, 5, 1)

