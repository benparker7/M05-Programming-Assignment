import unittest

from __init__ import sum
from fractions import Fraction


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)


def test_list_fraction(self):
    """
    Test that it can sum a list of fractions
    """
    data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
    result = sum(data)
    self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()


# The test results of the programming assignment show that we can test our projects using test runners
# The results are good for me, but the tutorial says and shows that the output should create an error
