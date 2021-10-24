# Create class Worker with fields name and salary. If salary negative
# raise ValueError
#
# Create a method get_tax_value() that calculate tax from salary .
# Tax must be calculate like "progressive tax" with next step:
#
# less then 1000 - 0%
# 1001 - 3000 - 10%
# 3001 - 5000 - 15%
# 5001 - 10000 - 21%
# 10001 - 20000 - 30%
# 20001 - 50000 - 40%
# more than 50000 - 47%
# Please create WorkerTest class with unitest to the class Worker.
# Try to use setUp and tearDown methods. Don`t use assertRaises in tests.
import unittest


class Worker:
    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary

    def get_tax_value(self):
        res = []
        salary = self.salary
        if salary < 1000:
            res.append(0)
        elif 1001 <= salary <= 3000:
            res.append(0.1 * (salary - 1000))
        elif 3001 < salary < 5000:
            res.append(0.15 * (salary - 3000))
        elif 5001 < salary < 10000:
            res.append(0.21 * (salary - 5000))
        elif 10001 < salary < 20000:
            res.append(0.3 * (salary - 10000))
        elif 20001 < salary < 50000:
            res.append(0.4 * (salary - 20000))
        elif salary > 50000:
            res.append(0.47 * (salary - 50000))
        return sum(res)

class WorkerTest(unittest.TestCase):
    pass