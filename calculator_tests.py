import unittest

from calculator import get_hypotenuse, get_area


class CalculatingHypotenuseTestCase(unittest.TestCase):
    def test_case_1(self):
        res = get_hypotenuse(3, 4)
        self.assertEqual(res, 5)

    def test_case_2(self):
        res = get_hypotenuse(5, 12)
        self.assertEqual(res, 13)

    def test_case_3(self):
        res = get_hypotenuse(8, 15)
        self.assertEqual(res, 17)

class CalculatingAreaTestCase(unittest.TestCase):
    def test_case_1(self):
        res = get_area(3, 4)
        self.assertEqual(res, 6)

    def test_case_2(self):
        res = get_area(5, 12)
        self.assertEqual(res, 30)

    def test_case_3(self):
        res = get_area(8, 15)
        self.assertEqual(res, 60)