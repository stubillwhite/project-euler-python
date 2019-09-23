from problem001 import *
import unittest

# Pull in the built-in Python testing framewkr
class Problem1TestCase(unittest.TestCase):

    def test_sum_of_divisible_naturals(self):
        self.assertEqual(sum_of_divisible_naturals(10), 23)
