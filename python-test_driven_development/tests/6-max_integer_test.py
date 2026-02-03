#!/usr/bin/python3
"""
Unitests.
"""
import unittest
max_integer = __import__('6-max_integer').max_integer
class TestMaxInteger(unittest.TestCase):
    """
    Testes.
    """

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        self.assertEqual(max_integer([5]), 5)

    def test_positive_integers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_integers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_integers(self):
        self.assertEqual(max_integer([-10, 0, 5, 3]), 5)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([10, 2, 3, 4]), 10)

    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 10]), 10)

    def test_repeated_max(self):
        self.assertEqual(max_integer([3, 3, 3]), 3)

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.7, 2.6]), 2.7)

    def test_mixed_int_float(self):
        self.assertEqual(max_integer([1, 2.5, 2]), 2.5)

    def test_string(self):
        self.assertEqual(max_integer("abc"), "c")

    def test_list_of_strings(self):
        self.assertEqual(max_integer(["apple", "banana", "pear"]), "pear")

if __name__ == "__main__":
    unittest.main()
