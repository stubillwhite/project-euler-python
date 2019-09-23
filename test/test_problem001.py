from problem001 import *
import unittest

# Pull in the built-in Python testing framework
class Problem1TestCase(unittest.TestCase):

    # Tests need to begin with test_ to be found
    def test_sum_of_divisible_naturals(self):
        self.assertEqual(sum_of_divisible_naturals(10), 23)
