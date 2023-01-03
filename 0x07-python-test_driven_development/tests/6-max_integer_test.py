#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unit test for the max_integer function"""

    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_first(self):
        self.assertEqual(max_integer([6, 2, 4, 5, 2]), 6)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_one_element(self):
        self.assertEqual(max_integer([4]), 4)

    def test_floats(self):
        self.assertEqual(max_integer([1.1, 4.5, 3.8, 7.2, 6.9]), 7.2)


if __name__ == '__main__':
    unittest.main()
