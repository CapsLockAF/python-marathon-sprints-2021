# Create class Triangle with method get_area() that calculate area of
# triangle. As input you will have list of 3 sides size
# Examples:
# triangle = Triangle([3, 3, 3])
# Use classes TriangleNotValidArgumentException and
# TriangleNotExistException
# Create class TriangleTest with unittest and subTest()
# context manager for class Triangle.

# test data:
# valid_test_data = [
#     ((3, 4, 5), 6.0),
#     ((10, 10, 10), 43.30),
#     ((6, 7, 8), 20.33),
#     ((7, 7, 7), 21.21),
#     ((50, 50, 75), 1240.19),
#     ((37, 43, 22), 406.99),
#     ((26, 25, 3), 36.0),
#     ((30, 29, 5), 72.0),
#     ((87, 55, 34), 396.0),
#     ((120, 109, 13), 396.0),
#     ((123, 122, 5), 300.0)
# ]
# not_valid_triangle = [
#     (1, 2, 3),
#     (1, 1, 2),
#     (7, 7, 15),
#     (100, 7, 90),
#     (17, 18, 35),
#     (127, 17, 33),
#     (145, 166, 700),
#     (1000, 2000, 1),
#     (717, 17, 7),
#     (0, 7, 7),
#     (-7, 7, 7)
# ]
# not_valid_arguments = [
#     ('3', 4, 5),
#     ('a', 2, 3),
#     (7, "str", 7),
#     ('1', '1', '1'),
#     'string',
#     (7, 2),
#     (7, 7, 7, 7),
#     'str',
#     10,
#     ('a', 'str', 7)
# ]
import unittest


class TriangleNotValidArgumentException(Exception):
    def __str__(self):
        return "Not valid arguments"


class TriangleNotExistException(Exception):
    def __str__(self):
        return "Can`t create triangle with this arguments"


class Triangle:
    def __init__(self, sides):
        self.is_valid_argument(sides)
        self.is_exist_trangle(sides)
        self.sides = sides


    def is_valid_argument(self, sizes):
        if not type(sizes) == tuple or not len(
                [i for i in sizes if type(i) == int]) == 3:
            raise TriangleNotValidArgumentException

    def is_exist_trangle(self, sizes):
        if sizes[0] + sizes[1] > sizes[2] and sizes[1] + sizes[2] > sizes[0] and sizes[0] + sizes[2] > sizes[1]:
            return
        raise TriangleNotExistException

    def get_area(self):
        sizes = self.sides
        p = sum(self.sides) / 2
        return (p * (p - sizes[0]) * (p - sizes[1]) * (
                    p - sizes[2])) ** 0.5


class TriangleTest(unittest.TestCase):
    def test_with_valid_test_data(self):
        valid_test_data = [
            ((3, 4, 5), 6.0),
            ((10, 10, 10), 43.30),
            ((6, 7, 8), 20.33),
            ((7, 7, 7), 21.21),
            ((50, 50, 75), 1240.19),
            ((37, 43, 22), 406.99),
            ((26, 25, 3), 36.0),
            ((30, 29, 5), 72.0),
            ((87, 55, 34), 396.0),
            ((120, 109, 13), 396.0),
            ((123, 122, 5), 300.0)
        ]
        for data in valid_test_data:
            triangle = Triangle(data[0])
            with self.subTest():
                self.assertEqual(round(triangle.get_area()), round(data[1]))

    def test_exception_triangle_not_exist(self):
        not_valid_triangle = [
            (1, 2, 3),
            (1, 1, 2),
            (7, 7, 15),
            (100, 7, 90),
            (17, 18, 35),
            (127, 17, 33),
            (145, 166, 700),
            (1000, 2000, 1),
            (717, 17, 7),
            (0, 7, 7),
            (-7, 7, 7)
        ]
        for data in not_valid_triangle:
            with self.subTest():
                with self.assertRaises(TriangleNotExistException):
                    Triangle(data)

    def test_exception_not_valid_arguments(self):
        not_valid_arguments = [
            ('3', 4, 5),
            ('a', 2, 3),
            (7, "str", 7),
            ('1', '1', '1'),
            'string',
            (7, 2),
            (7, 7, 7, 7),
            'str',
            10,
            ('a', 'str', 7)
        ]
        for data in not_valid_arguments:
            with self.subTest():
                with self.assertRaises(TriangleNotValidArgumentException):
                    Triangle(data)

